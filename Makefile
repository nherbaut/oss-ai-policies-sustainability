SRC := protocol.md
PDF := $(SRC:.md=.pdf)

all: $(PDF)

%.pdf: %.md refs.bib
	pandoc $< -o $@ --citeproc --bibliography=refs.bib --pdf-engine=xelatex -V geometry:margin=2.5cm -V fontsize=11pt -V colorlinks=true

clean:
	rm -f $(PDF)

# See CODING.md. Export arguments as data rather than interpolating them in shell code.
export PR BRANCH SESSION RESOLUTIONS

coding:
	@bash scripts/coding-session.sh

coding-start:
	@bash scripts/coding-session.sh start

coding-setup:
	@bash scripts/coding-session.sh setup

coding-protect:
	@bash scripts/coding-session.sh protect

coding-finish:
	@bash scripts/coding-session.sh finish

coding-request-merge:
	@if [ -n "$$SESSION" ]; then \
		bash scripts/coding-session.sh request-merge --session "$$SESSION"; \
	else \
		bash scripts/coding-session.sh request-merge; \
	fi

coding-status:
	@bash scripts/coding-session.sh status

coding-integrate:
	@if [ -n "$$PR" ] && [ -z "$$BRANCH" ]; then \
		bash scripts/coding-session.sh integrate "$$PR"; \
	elif [ -n "$$BRANCH" ] && [ -z "$$PR" ]; then \
		bash scripts/coding-session.sh integrate --branch "$$BRANCH"; \
	else \
		printf '%s\n' 'Use make coding-integrate PR=123 or make coding-integrate BRANCH=coding/...' >&2; \
		exit 2; \
	fi

coding-sync:
	@bash scripts/coding-session.sh sync

coding-codebook-init:
	@bash scripts/coding-session.sh codebook-init

coding-codebook-register:
	@bash scripts/coding-session.sh codebook-register

coding-theory-publish:
	@bash scripts/coding-session.sh theory-publish --branch "$$BRANCH"

coding-test:
	python3 -B -m unittest discover -s scripts/tests -v
	node scripts/tests/test_coding_action.cjs
	bash -n scripts/coding-session.sh
	@for hook in .githooks/*; do sh -n "$$hook" || exit; done

# Static, read-only snapshot of the current checkout's QualCoder project.
coding-site:
	python3 -B scripts/build_coding_site.py

.PHONY: coding-site

.PHONY: all clean coding coding-start coding-setup coding-protect coding-finish coding-request-merge coding-status coding-integrate coding-test

.PHONY: coding-sync coding-codebook-init coding-codebook-register coding-theory-publish
