.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= 01_intro.pdf 02_prelims.pdf 03_ipython_plotting.pdf \
  04_saving_scripts.pdf \
	05_lists_arrays.pdf \
	06_numpy.pdf \
	07_more_numpy.pdf \
	08_basic_scipy.pdf \
	09_exercises.pdf \
  10_mlab.pdf \
  11_notebook.pdf

all: 	$(SLIDES) quickref.pdf

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
