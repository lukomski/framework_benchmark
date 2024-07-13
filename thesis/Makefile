xelatex : clean
	xelatex EE-dyplom
	biber EE-dyplom
	makeglossaries EE-dyplom
	xelatex EE-dyplom
	xelatex EE-dyplom

pdf:
	pdflatex  -interaction=nonstopmode  -output-directory="latex-out"  EE-dyplom.tex
	biber ./latex-out/EE-dyplom
	makeglossaries -d ./latex-out EE-dyplom
	pdflatex  -interaction=nonstopmode  -output-directory="latex-out"  EE-dyplom.tex
	pdflatex  -interaction=nonstopmode  -output-directory="latex-out"  EE-dyplom.tex
	cp latex-out/EE-dyplom.pdf .