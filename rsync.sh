#!/bin/bash -v
#export docs_repo=/Users/phil/repos/numeric_docs
#export labs_repo=/Users/phil/repos/numeric

rsync -avz _build/* piphome:/home/phil/public_html/numeric/.
# rsync -avz html_files/* piphome:/home/phil/public_html/numeric/.
#Rsync -avz pdf_files/* piphome:/home/phil/public_html/numeric/.
rsync -avz $docs_repo/pdf_create/_build/*pdf $docs_repo/pdf_files/.
rsync -avz $docs_repo/pdf_files/* $docs_repo/pdf_files/.
rsync -avz $docs_repo/html_files/* $docs_repo/html_files/.
#
# now copy to server
#
rsync -avz $docs_repo/pdf_create/_build/*pdf piphome:/home/phil/public_html/numeric/pdf_files/.
rsync -avz $docs_repo/pdf_files/* piphome:/home/phil/public_html/numeric/pdf_files/.
rsync -avz $docs_repo/html_files/* piphome:/home/phil/public_html/numeric/html_files/.
# ssh piphome 'chmod a+r /home/phil/public_html/numeric/pdf_files/*'
# ssh piphome -v 'ls -ldt /home/phil/public_html/numeric/pdf_files/* | head -30'
