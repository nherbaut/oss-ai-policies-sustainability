SRC := protocol.md
PDF := $(SRC:.md=.pdf)

all: $(PDF)

%.pdf: %.md refs.bib
	pandoc $< -o $@ --citeproc --bibliography=refs.bib --pdf-engine=xelatex -V geometry:margin=2.5cm -V fontsize=11pt -V colorlinks=true

clean:
	rm -f $(PDF)

PREFILTER_PYTHON ?= python3

prefilter-duplicates:
	$(PREFILTER_PYTHON) -B scripts/detect_document_duplicates.py

prefilter-similarity:
	$(PREFILTER_PYTHON) -B scripts/compute_rq_similarity.py

prefilter-test:
	$(PREFILTER_PYTHON) -B -m unittest discover -s scripts/tests -p 'test_prefilter*.py' -v

.PHONY: prefilter-duplicates prefilter-similarity prefilter-test

.PHONY: all clean
