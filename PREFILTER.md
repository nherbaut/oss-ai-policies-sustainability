# Préfiltrer le corpus avant codage

Les outils lisent les textes stockés dans `data/coding.qda/data.qda`, avec un
instantané SQLite cohérent en lecture seule. Ils ne modifient ni le projet
QualCoder, ni les documents, ni le codage, ni les anciens rapports d'analyse.
Les scores indiquent une proximité sémantique, pas une probabilité de pertinence.
Aucun document n'est supprimé ou automatiquement exclu.

## 1. Repérer les textes identiques

```sh
make prefilter-duplicates
```

Ce script utilise uniquement la bibliothèque standard de Python 3.10+.
`analysis/prefilter/duplicates.json` décrit les groupes et
`analysis/prefilter/duplicates.csv` recense toutes les occurrences. L'identité
porte sur le texte stocké, encodé en UTF-8, sans normaliser espaces, casse ou
retours à la ligne. Le SHA-256 sert à regrouper, puis l'égalité est vérifiée.
Le représentant est le plus petit identifiant QualCoder, sans préférence
analytique pour son projet. Les textes vides et les sources non textuelles sont
signalés séparément. Des textes proches mais différents ne sont pas des doublons
exacts pour cet outil.

Autres emplacements :

```sh
python3 -B scripts/detect_document_duplicates.py \
  --project data/coding.qda --output-dir analysis/prefilter/duplicates
```

## 2. Classer les documents par RQ

Les embeddings nécessitent `sentence-transformers` et NumPy. Pour un environnement
isolé, sans modifier les dépendances du workflow de codage :

```sh
python3 -m venv .venv-prefilter
.venv-prefilter/bin/python -m pip install -r scripts/requirements-prefilter.txt
make prefilter-similarity PREFILTER_PYTHON=.venv-prefilter/bin/python
```

Avec les dépendances déjà installées, utiliser simplement
`make prefilter-similarity`. Le modèle `intfloat/multilingual-e5-base` est fixé à
la révision `835193815a3936a24a0ee7dc9e3d48c1fbb19c55`. Par défaut, le calcul
utilise le CPU, des lots de 16 et uniquement les fichiers du cache Hugging Face.
Si le modèle n'est pas disponible, autoriser explicitement son téléchargement :

```sh
python3 -B scripts/compute_rq_similarity.py --allow-download
```

Les textes ne sont pas envoyés à une API. Le CPU peut prendre du temps pour le
corpus complet ; l'avancement est affiché par texte unique. Pour vérifier
l'installation sur les trois premiers documents :

```sh
python3 -B scripts/compute_rq_similarity.py \
  --limit 3 --batch-size 4 --output-dir analysis/prefilter/smoke
```

### Requêtes et représentation

Les RQ scientifiques restent dans `protocol.md`. Les requêtes autonomes de
`scripts/prefilter_queries.json` ne contiennent pas les hypothèses : une requête
générale et cinq facettes pour RQ1–RQ3 ; une requête générale, les limites
écologiques, la substituabilité et les arbitrages pour RQ4. La portée reste
la mission du projet pour RQ1, les politiques IA pour RQ2–RQ4.

Les paragraphes sont regroupés dans une fenêtre de **256 tokens d'entrée au
maximum**, préfixe `passage:`, contexte de titre et tokens spéciaux compris.
Un paragraphe trop long est subdivisé, sans perte de texte. Les titres Markdown
ATX sont reconnus hors des blocs de code ; les 32 premiers tokens du titre de
section immédiat sont ajoutés comme contexte. Le titre original reste intégralement
présent dans le texte source. Le chevauchement vaut zéro par défaut. La limite
effective du modèle (512 tokens pour E5) est toujours vérifiée.

Chaque bloc produit un vecteur normalisé. Le vecteur du document est la moyenne
des vecteurs de ses blocs, pondérée par le nombre de tokens de contenu source,
puis normalisée. Le contexte artificiel n'augmente pas ce poids. Avec un
chevauchement expérimental, le poids compte seulement le contenu nouvellement
couvert ; cela limite la répétition sans supprimer son effet sur les embeddings.

Les requêtes portent le préfixe `query:`. Le score global d'un document pour une
RQ est le **maximum des cosinus** entre son vecteur global et les différentes
requêtes de cette RQ. Un indicateur auxiliaire conserve aussi le meilleur couple
bloc–requête et son extrait exact. Les positions d'extrait sont des indices Python
en caractères, début inclus et fin exclue ; ce ne sont pas des positions QualCoder
UTF-16. Le score global reste le critère principal du classement.

### Fichiers produits

Tout `analysis/prefilter/` est ignoré par Git, y compris les caches et annotations.
Conserver séparément les annotations humaines avant de supprimer ce dossier.

| Fichier | Contenu |
| --- | --- |
| `scores.csv` | Une ligne par document, rang général, quatre scores et rangs, requêtes gagnantes, meilleurs passages, groupes de doublons. |
| `ranking-RQ1.csv` à `ranking-RQ4.csv` | Les mêmes lignes triées pour chaque RQ. |
| `embeddings.npz` | `document_ids`, `document_vectors`, `query_ids`, `query_vectors`, sans objets Python sérialisés. |
| `manifest.json` | RQ, paramètres, empreintes du corpus, révision, versions logicielles et compteurs. |
| `cache/` | Vecteurs réutilisables par contenu et paramètres ; les doublons partagent leur calcul. |
| `annotation.csv` | Échantillon d'au plus 60 contenus uniques, labels initialement vides. |
| `annotation-texts.json` | Texte intégral et provenance de cet échantillon, sans scores. |

Les cosinus restent dans `[-1, 1]`, sans conversion en pourcentage de pertinence.
Les contenus vides ont des scores et rangs non renseignés. Les égalités sont
départagées par identifiant. Le maximum général sert seulement à parcourir le
corpus : les nombres et formulations de requêtes diffèrent entre RQ, donc ses
scores ne permettent pas de comparer leur prévalence. Une moyenne globale peut
diluer un passage pertinent dans un long document ; consulter le score auxiliaire.

## 3. Comparer les réglages après annotation humaine

Pour une expérience reproductible, conserver les résultats dans des dossiers
distincts et partager le cache. Par exemple :

```sh
python3 -B scripts/compute_rq_similarity.py --chunk-tokens 256 \
  --output-dir analysis/prefilter/expanded-256 --cache-dir analysis/prefilter/cache
python3 -B scripts/compute_rq_similarity.py --chunk-tokens 480 \
  --output-dir analysis/prefilter/expanded-480 --cache-dir analysis/prefilter/cache
python3 -B scripts/compute_rq_similarity.py --query-mode original --chunk-tokens 256 \
  --output-dir analysis/prefilter/original-256 --cache-dir analysis/prefilter/cache
```

Pour un plan factoriel complet, ajouter aussi `--query-mode original` avec
`--chunk-tokens 480`. `--overlap-tokens 32`, `--device cuda` et `--batch-size`
permettent d'autres essais ; `--help` décrit les entrées. Les clés de cache
incluent le contenu, le modèle, la révision, le découpage et les paramètres de
calcul. Une modification des requêtes conserve les embeddings des documents.

**Utiliser un seul échantillon de référence pour toutes les expériences.** Celui
du premier calcul est stratifié par rôle du document, longueur et tiers du
classement général, avec graine 42. Les 60 contenus uniques sont répartis en
40 pour le réglage (`tuning`) et 20 pour l'évaluation (`evaluation`), ou moins
si le corpus disponible est plus petit. Les occurrences identiques ne sont
jamais réparties entre les deux ensembles.

Annoter les colonnes `RQ1_label` à `RQ4_label` de ce premier `annotation.csv`
avec `useful`, `not_useful` ou `uncertain`, en consultant `annotation-texts.json`.
Le script ne remplit aucun label et ne remplace pas les annotations existantes
lors d'un nouveau calcul. Utiliser un nouveau dossier si le corpus change.

```sh
python3 -B scripts/evaluate_prefilter.py \
  --annotations analysis/prefilter/expanded-256/annotation.csv \
  --runs analysis/prefilter/expanded-256 analysis/prefilter/expanded-480 \
    analysis/prefilter/original-256 \
  --budgets 5 10
```

L'évaluation refuse les labels incomplets, les doublons d'annotation, les
empreintes périmées et les corpus différents. Elle calcule précision et rappel
pour les premiers 5 et 10 documents **au sein de chaque sous-échantillon annoté**,
par RQ et par ensemble. Les cas incertains sont dénombrés mais exclus des
dénominateurs ; un rappel sans positif connu reste non renseigné.
Ces métriques ne sont pas des estimations du rappel sur les 600 documents.
Choisir les réglages sur `tuning`, puis consulter `evaluation` une fois le choix
fixé. Aucun seuil d'exclusion n'est déduit automatiquement.

## Tests

```sh
make prefilter-test
```

Les tests utilisent de petites bases SQLite et un modèle simulé ; ils ne
téléchargent aucun modèle et ne changent pas la base de recherche. Les tests
vectoriels sont ignorés si NumPy n'est pas installé. Aucune dépendance de calcul
d'embeddings ni étape de préfiltrage n'est ajoutée au déploiement Pages.
