.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= intro.pdf prelims.pdf ipython_plotting.pdf \
  saving_scripts.pdf \
	lists_arrays.pdf \
	numpy.pdf \
	more_numpy.pdf \
	basic_scipy.pdf \
	exercises.pdf \
  mlab.pdf \
  notebook.pdf

all: 	$(SLIDES) quickref.pdf

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
