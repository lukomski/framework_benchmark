
Go to proper directory:
```
cd /home/jan/Dokumenty/Studia/MSem3/Magisterka/sandbox/framework-benchmark/thesis
```

Buld PDF
```
pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory="latex-out"  "/home/jan/Dokumenty/Studia/MSem3/Magisterka/sandbox/framework-benchmark/thesis/EE-dyplom.tex"
```

Copy generated file:
```
cp latex-out/EE-dyplom.pdf .
```