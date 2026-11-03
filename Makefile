SRC := protocol.md
PDF := $(SRC:.md=.pdf)

all: $(PDF)

%.pdf: %.md refs.bib
	pandoc $< -o $@ --citeproc --bibliography=refs.bib --pdf-engine=xelatex -V geometry:margin=2.5cm -V fontsize=11pt -V colorlinks=true

clean:
	rm -f $(PDF)

.PHONY: all clean
