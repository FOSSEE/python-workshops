.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= 1_intro.pdf \
			  2_names_objects.pdf \
        3_varargs_kwargs.pdf \
				4_only_kwargs.pdf \
        5_closures.pdf \
        6_practice_functions.pdf \
				7_oop_basics.pdf \
				8_oop_inheritance.pdf \
				9_oop_containership.pdf \
				10_oop_classattr.pdf \
				11_oop_misc.pdf \
				12_oop_simple_special_methods.pdf \
        13_oop_special_methods.pdf

all:    $(SLIDES)

cleanall: clean
	rm -f *.dvi *.ps *.eps *.pdf

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
