#!/bin/bash

cat dhh1.txt dhh-2.txt dhh-3.txt dhh-4.txt > dhh.txt
#Limpiar de notas y otras referencias
perl -ne "print unless /\d+\. \d+\.|NOTAS:|Advertencia|http:|\([0-9\s\.\-a-zA-Z;]+\)/" dhh.txt > dhhsinnotas.txt
tr -s "\[[:digit:]\]" " " < dhhsinnotas.txt > dhhsinnotas1.txt
#Una línea por frase
tr -s "[:digit:]" "\n" < dhhsinnotas1.txt > dhhlimpio.txt
sed '/^\s*$/d' dhhlimpio.txt > dhh.txt
