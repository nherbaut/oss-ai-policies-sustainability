[published](https://github.com/oxidecomputer/rfd/pull/964)

RFD 576

# RFD 576 Using LLMs at Oxide

This RFD can be accessed by the following groups:\[public\]

State

published

RFD

576

Authors

[Bryan Cantrill](/?author=bryan%40oxide.computer)

Updated

Large language models (LLMs) are an indisputable breakthrough of the last five years, potentially profoundly changing the way that we work. As with any extraordinarily powerful tool, LLM use has both promise and peril — and that they are so general-purpose leaves real questions about how and when they should be used. The landscape is shifting so rapidly that static prescription is unlikely — but that LLMs are evolving so quickly also gives urgency to the question: **how should LLMs be used at Oxide**?

## [Values in LLM](#_values_in_llm_usage)

usage

As is our wont, it’s helpful to look at LLM use through the lens of our values, several of which come to mind, listed here in priority order:

- **Responsibility**: In terms of LLM use at Oxide, our lodestar is our sense of responsibility. However powerful they may be, LLMs are but a tool, ultimately acting at the behest of a human. Oxide employees bear responsibility for the artifacts we create, whatever automation we might employ to create them. That is, human judgement remains firmly in the loop: even if or as an LLM is generating an artifact that we will use (writing, test cases, documentation, code, etc.), their output is the responsibility of the human using them.

- **Rigor**: LLMs are double-edged with respect to rigor. On the one hand, wielded carefully, they can help us sharpen our own thinking by pointing out holes in our own reasoning or otherwise providing thought-provoking suggestions. On the other, if used recklessly or thoughtlessly, they can have the opposite effect, replacing crisp thinking with generated flotsam. LLMs are useful in as much as they promote and reinforce our rigor.

- **Empathy**: Be we readers or writers, there are humans on the other end of our language use. As we use LLMs, we must keep in mind our empathy for that human, be they the one who is consuming our writing, or the one who has written what we are reading.

- **Teamwork**: We are working together on a shared endeavor, and we must be sure that our LLM use does not undermine our sense of teamwork. Specifically, we must be careful to not use LLMs in such a way as to undermine the trust that we have in one another. In some cases, LLM usage is going to be warranted (or otherwise expected), and in others it won’t be. Note this isn’t as simple as disclosure of usage: in some contexts, volunteering that an LLM has been used to generate work product may implicitly distance oneself from the responsibility for the content — and erode the trust that is essential for teamwork.

- **Urgency**: Urgency seems natural with a tool that can seemingly do so much knowledge work so quickly, but with respect to LLM use, too many organizations have seemingly enshrined urgency over all else. These organizations treat LLMs as an opportunity to increase pace over all else, seemingly without regard for setting direction. Urgency is certainly important, and LLMs absolutely afford an opportunity to do work more quickly — but that pace must not come at the expense of our responsibility, rigor, empathy and teamwork.

## [Uses of LLMs](#_uses_of_llms)

LLM use varies widely, and the ramifications of those uses vary accordingly; it’s worth taking apart several of the (many) uses for LLMs.

### [LLMs as readers](#_llms_as_readers)

LLMs are superlative at reading comprehension, able to process and meaningfully comprehend documents effectively instantly. This can be extraordinarily powerful for summarizing documents — or of answering more specific questions of a large document like a datasheet or specification. (Ironically, LLMs are especially good at evaluating documents to assess the degree that an LLM assisted their creation!)

While use of LLMs to assist comprehension has little downside, it does come with an important caveat: when uploading a document to a hosted LLM (ChatGPT, Claude, Gemini, etc.), there must be assurance of **data privacy** — and specifically, assurance that the model will not use the document to train future iterations of itself. Note that this may be opt-out (that is, by default, a model may reserve the right to train on uploaded documents), but can generally be controlled via preferences — albeit occasionally via euphemism. (OpenAI shamelessly calls this checked-by-default setting "Improve the model for everyone", making anyone who doesn’t wish the model to train on their data feel as if they suffer from a kind of reactionary avarice.)

A final cautionary note: using LLMs to assist comprehension should not substitute for actually reading a document where such reading is socially expected. More concretely: while LLMs can be a useful tool to assist in the evaluating of candidate materials per [\[rfd3\]](/rfd/0003), their use should be restricted to be as a tool, not as a substitute for human eyes (and brain!).

### [LLMs as](#_llms_as_researchers)

researchers

LLMs can be useful researchers. LLMs are well-suited for the kind of light research tasks for which one would historically use an internet search engine, especially as LLM hallucination has been attenuated and sourcing has improved (and, frankly, as the quality of Google search results has declined).

For more involved research, LLMs are still useful, but with a cautionary note: the quality of results can vary widely based on model, level of reasoning, quality of prompt, etc., and one should be careful about drawing too much confidence from the lengthy, well-formatted nature of an LLM-powered report. Even if a report appears well-sourced, one shouldn’t assume that the sources themselves are correct; as LLM-authored content is increasingly found in the wild, a seemingly authoritative source found by an LLM may itself be an LLM hallucination! (In particular, it is not uncommon to find LLM-derived research that makes fantastical claims about Oxide, including products we don’t offer or capabilities we don’t have.)

When engaging LLMs as researchers, one should select a model with deep research capabilities enabled, following its citation links to learn more from the original sources. One should not trust or share LLM-researched content without checking it first; it should be treated as a jumping off point to kickstart one’s own research efforts rather than a finished product.

Finally, as with any other use of LLMs, the responsibility for the artifact lies with the person using the LLM to aid their research, not with the LLM itself.

### [LLMs as editors](#_llms_as_editors)

LLMs can be excellent editors. Engaging an LLM late in the creative process (that is, with a document already written and broadly polished), allows for LLMs to provide helpful feedback on structure, phrasing, etc. — all without danger of losing one’s own voice. A cautionary note here: LLMs are infamous pleasers — and you may find that the breathless praise from an LLM is in fact more sycophancy than analysis. This becomes more perilous the earlier one uses an LLM in the writing process: the less polish a document already has, the more likely it is that an LLM will steer to something wholly different — at once praising your groundbreaking genius while offering to rewrite it for you.

### [LLMs as writers](#_llms_as_writers)

While LLMs are adept at reading and can be terrific at editing, their writing is much more mixed. At best, writing from LLMs is hackneyed and cliché-ridden; at worst, it brims with tells that reveal that the prose is in fact automatically generated.

What’s so bad about this? First, to those who can recognize an LLM’s reveals (an expanding demographic!), it’s just embarrassing — it’s as if the writer is walking around with their [intellectual fly open](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/). But there are deeper problems: LLM-generated writing undermines the authenticity of not just one’s writing but of the thinking behind it as well. If the prose is automatically generated, might the ideas be too? The reader can’t be sure — and increasingly, the hallmarks of LLM generation cause readers to turn off (or worse).

Finally, LLM-generated prose undermines a social contract of sorts: absent LLMs, it is presumed that of the reader and the writer, it is the writer that has undertaken the greater intellectual exertion. (That is, it is more work to write than to read!) For the reader, this is important: should they struggle with an idea, they can reasonably assume that the writer themselves understands it — and it is the least a reader can do to labor to make sense of it.

If, however, prose is LLM-generated, this social contract becomes ripped up: a reader cannot assume that the writer understands their ideas because they might not so much have read the product of the LLM that they tasked to write it. If one is lucky, these are LLM hallucinations: obviously wrong and quickly discarded. If one is unlucky, however, it will be a kind of LLM-induced cognitive dissonance: a puzzle in which pieces don’t fit because there is in fact no puzzle at all. This can leave a reader frustrated: why should they spend more time reading prose than the writer spent writing it?

This can be navigated, of course, but it is truly perilous: our writing is an important vessel for building trust — and that trust can be quickly eroded if we are not speaking with our own voice. For us at Oxide, there is a more mechanical reason to be jaundiced about using LLMs to write: because our hiring process very much selects for writers, we know that everyone at Oxide **can** write — and we have the luxury of demanding of ourselves the kind of writing that we know that we are all capable of.

So our guideline is to generally **not** use LLMs to write — but there is nuance here, and different kinds of writing merit some elaboration.

#### [LLMs in public](#_llms_in_public_writing)

writing

The prevalence of LLM-infused writing (and the concomitant loss of reader trust) has made the potential consequences of LLM use in public writing much more dire: if the reader believes text to be LLM-authored, they are increasingly likely to not only stop reading, but to question the writer. And when the writer is representing Oxide — as is the case for public writing like a company blog post, press release, social media post, or public RFD — it is the authenticity of Oxide’s voice itself that becomes suspect.

We must not endanger the Oxide voice that we have all worked so hard to build: for any public Oxide writing, not only must an LLM not be used to write, but it must be **further** true that the text not be read as LLM-authored. This is a higher bar, and arguably a weirder one: not only must it be human written, it must be unimpeachably so.

Fortunately, tools can help. We use Pangram at Oxide, and have found its false positive rate to be extremely low.[\[pangram4\]](https://arxiv.org/abs/2607.27183) Before publication, Pangram should report that the writing is entirely human-written. Note that it is possible — though in our experience, highly unlikely — that human-authored text will need to be slightly re-worked to achieve this. (Much more likely, however, is that Pangram successfully identifies clauses or paragraphs that were indeed LLM-authored, if perhaps as the innocent result of accepting an LLM’s suggestion during the editing process.)

#### [LLMs in personal](#_llms_in_personal_writing)

writing

For any writing where the expectation is clearly direct personal communication — e.g., chat, review comments, e-mail — LLMs should never be used to write. This is not to say that LLMs will not be used at all: they can be used to inform (in the case of review comments) or edit (e-mails) — but they should never be used to write text that the reader is very clearly expecting to be human-authored.

#### [LLMs in](#_llms_in_operational_writing)

operational writing

If the guidelines for LLM use in public writing and personal writing are clear (namely: don’t), it’s quite a bit murkier for the workhorse writing that serves to get a job done. This is *operational writing*: it is neither highfalutin prose nor quotidian correspondence, but rather the kind of writing that documents an aspect of the system or contains the detailed response to an RFP. For operational writing, accuracy and completeness trump all else: the reader’s expectation is correctness, not authorship. (Indeed, a hallmark of operational writing is that its attribution to an author is incidental, if it’s attributed at all.) As a result, LLMs may find use in the mechanics of operational writing (including the generation of text), but the human author remains accountable: correctness must be verified — and responsibility to the reader is paramount.

### [LLMs as code](#_llms_as_code_reviewers)

reviewers

As with reading comprehension and editing, LLMs can make for good code reviewers. But they can also make nonsense suggestions or otherwise miss larger issues. LLMs should be used for review (and can be very helpful when targeted to look for a particular kind of issue), but that review should not be accepted as a human substitute.

### [LLMs as debuggers](#_llms_as_debuggers)

LLMs can be surprisingly helpful debugging problems, but perhaps only because our expectations for them would be so low. While LLMs shouldn’t be relied upon (clearly?) to debug a problem, they can serve as a kind of animatronic [rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging), helping to inspire the next questions to ask. (And they can be surprising: LLMs have been known to debug I2C issues from the screenshot of a scope capture!) When debugging a vexing problem one has little to lose by using an LLM (provided, of course, it does not displace interactions with one’s colleagues to collaboratively debug!) — but perhaps also little to gain.

### [LLMs as](#_llms_as_programmers)

programmers

LLMs are amazingly good at writing code — so much so that there is borderline mass hysteria about LLMs entirely eliminating software engineering as a craft. As with using an LLM to write prose, there is obvious peril here! Unlike prose, however (which really should be handed in a polished form to an LLM to maximize the LLM’s efficacy), LLMs can be quite effective writing code *de novo*. This is especially valuable for code that is experimental or auxiliary or otherwise throwaway. The closer code is to the system that we ship, the greater care needs to be shown when using LLMs. Even with something that seems natural for LLM contribution (e.g., writing tests), one should still be careful: it’s easy for LLMs to spiral into nonsense on even simple tasks.

As with so many things, using LLMs to aid in programming requires judgement and balance: they can be extraordinarily useful across an entire spectrum of software activity, and shouldn’t be dismissed out of hand. But any implicit dependency on an LLM to comprehend or evolve a system must also be strenuously resisted: we do not want to become as gavage geese, being force-fed unnecessary complexity in hopes that an LLM will somehow spare us from asphyxiation.

Wherever LLM-generated code is used, it becomes the responsibility of the engineer. As part of this process of taking responsibility, **self-review** becomes essential: LLM-generated code should not be reviewed by others if the responsible engineer has not themselves reviewed it. Moreover, once in the loop of peer review, generation should more or less be removed: if code review comments are addressed by wholesale re-generation, iterative review becomes impossible.

In short, where LLMs are used to generate code, responsibility, rigor, empathy and teamwork must remain top of mind.

## [LLM anti-patterns](#_llm_anti_patterns)

There are some obvious pitfalls of LLM usage that are worth calling out, not because we at Oxide are in any particular danger of falling into them, but because others are (or seem to be) — and they constitute behavior that we absolutely want to avoid.

### [LLM mandates](#_llm_mandates)

LLMs are certainly valuable tools, but some organizations — either out of executive capriciousness, misguided micromanagement, or something darker — have mandated (or otherwise strongly incentivized) their organization’s use of LLMs. Such decrees are absurd: they undermine the autonomy and mastery essential in our work. As with any tool, we should feel empowered to use LLMs, but not obligated to do so: we trust ourselves to choose the best tool for the job, be it LLM or no.

Executive fiats with respect to LLM usage will not be forthcoming.

### [LLM shaming](#_llm_shaming)

Conversely, some have decided that they not only oppose LLM use for themselves, but wish to out or otherwise shame those that are making use of LLMs. Aside from the impracticalities of this position (e.g., as LLMs become the foundation for technologies like search, it will become increasingly difficult to attest to one’s own purity), such strident opposition undermines teamwork.

In this regard, LLM use may be viewed as a dietary choice: one may choose to (say) not eat meat — and at Oxide we wish to empathize with that disposition by making sure that vegetarian options are available when we eat together. But just as we accommodate those choices, those who make them must understand that others will make different decisions — and it is decidedly anti-social to interrupt someone’s meal to register disapproval with their choice of entrée.

### [LLM](#_llm_anthropomorphization)

anthropomorphization

LLMs can (obviously) feel human-like, which has inspired some to close the loop entirely, explicitly anthropomorphizing LLMs with a prompt that constitutes a persona. Especially when coupled with realistic (LLM-powered!) voice generation, the result can be uncanny — and perilous: an LLM is (emphatically!) not a person, and in particular cannot be held accountable; to anthropomorphize an LLM is to imply a responsibility that they cannot take. (For an amusing — and horrifying — treatment of the absolute chaos this can unleash, see the [Shell Game podcast](https://www.shellgame.co).)

However tempting anthropomorphizing LLMs may be, it’s not a practice that we will engage in at Oxide.

## [Mechanics](#_mechanics)

Mechanical details of using LLMs — along with many specific tips and links — can be found in the (internal) [LLMs at Oxide](https://github.com/oxidecomputer/meta/tree/master/engineering/llms) document.

## [Determinations](#_determinations)

Broadly speaking, LLM use is encouraged at Oxide, but that use must always be consistent with our deeply-held sense of responsibility: our responsibility to our product, our responsibility to our customers — and our responsibility to one another.

## [External](#_external_references)

References

- \[rfd3\] Oxide Computer Company. RFD 3 Oxide Hiring Process. [https://rfd.shared.oxide.computer/rfd/0003](/rfd/0003).

- \[pangram4\] Ben Glickenhaus, Katherine Thai, Jenna Russell, Elyas Masrour, Yue Han, Max Spero, and Bradley Emi, *Pangram 4 Technical Report*, [arXiv:2607.27183](https://arxiv.org/abs/2607.27183), 2026.

- \[Shell Game\] *Shell Game*, Season 2. [https://www.shellgame.co](https://www.shellgame.co)

- [Values in LLM usage](#_values_in_llm_usage)
- [Uses of LLMs](#_uses_of_llms)
- [LLMs as readers](#_llms_as_readers)
- [LLMs as researchers](#_llms_as_researchers)
- [LLMs as editors](#_llms_as_editors)
- [LLMs as writers](#_llms_as_writers)
- [LLMs in public writing](#_llms_in_public_writing)
- [LLMs in personal writing](#_llms_in_personal_writing)
- [LLMs in operational writing](#_llms_in_operational_writing)
- [LLMs as code reviewers](#_llms_as_code_reviewers)
- [LLMs as debuggers](#_llms_as_debuggers)
- [LLMs as programmers](#_llms_as_programmers)
- [LLM anti-patterns](#_llm_anti_patterns)
- [LLM mandates](#_llm_mandates)
- [LLM shaming](#_llm_shaming)
- [LLM anthropomorphization](#_llm_anthropomorphization)
- [Mechanics](#_mechanics)
- [Determinations](#_determinations)
- [External References](#_external_references)

### Table of Contents
