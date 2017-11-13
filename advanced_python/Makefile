.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= intro.pdf \
			  names_objects.pdf \
        varargs_kwargs.pdf \
				only_kwargs.pdf \
        closures.pdf

all:    $(SLIDES)

cleanall: clean
	rm -f *.dvi *.ps *.eps *.pdf

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
