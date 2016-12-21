.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= intro.pdf prelims.pdf session1a.pdf \
	session1b.pdf \
	session2.pdf \
	session3.pdf \
	session4.pdf \
  mlab.pdf

all: 	$(SLIDES) quickref.pdf

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
