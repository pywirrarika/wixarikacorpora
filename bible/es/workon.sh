#!/bin/bash
#
# GPL 3+ Manuel Mager
#
# We use dhh spanish bible. 
# wget http://web.archive.org/web/20091026194848/geocities.com/kubyimm1/dhh-2.zip
# wget http://web.archive.org/web/20091026194848/geocities.com/kubyimm1/dhh-2.zip
# wget http://web.archive.org/web/20091026194848/geocities.com/kubyimm1/dhh-2.zip
# wget http://web.archive.org/web/20091026194848/geocities.com/kubyimm1/dhh-2.zip
#

echo Cleaning dhh spanish bible...

cat dhh1.txt dhh-2.txt dhh-3.txt dhh-4.txt > dhh.txt

#Limpiar de notas y otras referencias
perl -ne "print unless /\d+\. \d+\.|NOTAS:|Advertencia|http:|\([0-9\s\.\-a-zA-Z;]+\)/" dhh.txt > dhhsinnotas.txt
tr -s "\[[:digit:]\]" " " < dhhsinnotas.txt > dhhsinnotas1.txt
#Una línea por frase
tr -s "[:digit:]" "\n" < dhhsinnotas1.txt > dhhlimpio.txt
sed '/^\s*$/d' dhhlimpio.txt > dhh.txt

echo Done!
