.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= 01_intro.pdf \
			  02_names_objects.pdf \
        03_varargs_kwargs.pdf \
				04_only_kwargs.pdf \
        05_closures.pdf \
        06_practice_functions.pdf \
				07_oop_basics.pdf \
				08_oop_inheritance.pdf \
				09_oop_containership.pdf \
				10_oop_classattr.pdf \
				11_oop_misc.pdf \
				12_oop_simple_special_methods.pdf \
        13_oop_special_methods.pdf

all:    $(SLIDES)

cleanall: clean
	rm -f *.dvi *.ps *.eps *.pdf

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
