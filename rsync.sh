#!/bin/bash -v
rsync -avz _build/* piphome:/home/phil/public_html/numeric/.
rsync -avz html_files piphome:/home/phil/public_html/numeric/.
rsync -avz pdf_files piphome:/home/phil/public_html/numeric/.

