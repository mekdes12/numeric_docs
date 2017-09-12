#!/bin/bash -v
#export numdocs=/Users/phil/repos/numeric_docs
#export numlabs=/Users/phil/repos/numeric

rsync -avz _build/* piphome:/home/phil/public_html/numeric/.
# rsync -avz html_files/* piphome:/home/phil/public_html/numeric/.
#Rsync -avz pdf_files/* piphome:/home/phil/public_html/numeric/.
rsync -avz $numdocs/pdf_create/_build/*pdf $numdocs/pdf_files/.
rsync -avz $numdocs/pdf_files/* $numdocs/pdf_files/.
rsync -avz $numdocs/html_files/* $numdocs/html_files/.
#
# now copy to server
#
rsync -avz $numdocs/pdf_create/_build/*pdf piphome:/home/phil/public_html/numeric/pdf_files/.
rsync -avz $numdocs/pdf_files/* piphome:/home/phil/public_html/numeric/pdf_files/.
rsync -avz $numdocs/html_files/* piphome:/home/phil/public_html/numeric/html_files/.
# ssh piphome 'chmod a+r /home/phil/public_html/numeric/pdf_files/*'
# ssh piphome -v 'ls -ldt /home/phil/public_html/numeric/pdf_files/* | head -30'
