.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= 01_basics.pdf \
  02_practice_basics.pdf \
  03_control_flow.pdf \
  04_practice_control_flow.pdf \
  05_core_data_structures.pdf \
  06_practice_ds.pdf \
  07_functions.pdf \
  08_practice_functions.pdf \
  09_modules.pdf \
  10_files.pdf \
  11_exceptions.pdf \
  12_practice_files_exc.pdf

all: 	$(SLIDES)

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm *.synctex.gz
