.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= basics.pdf \
  practice_basics.pdf \
  control_flow.pdf \
  practice_control_flow.pdf \
  core_data_structures.pdf \
  practice_ds.pdf

all: 	$(SLIDES)

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
