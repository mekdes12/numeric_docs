#!/bin/bash -v
rsync -avz _build/* piphome:/home/phil/public_html/numeric/.
rsync -avz html_files/* piphome:/home/phil/public_html/numeric/.
rsync -avz pdf_files/* piphome:/home/phil/public_html/numeric/.
rsync -avz /Users/phil/repos/numeric_docs/pdf_files/* /Users/phil/repos/numeric_docs/pdf_files/.
rsync -avz /Users/phil/repos/numeric_docs/html_files/* /Users/phil/repos/numeric_docs/html_files/.
ssh piphome 'chmod a+r /home/phil/public_html/numeric/pdf_files/*'
ssh piphome -v 'ls -ldt /home/phil/public_html/numeric/pdf_files/* | head -30'
