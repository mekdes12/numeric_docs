"""
assumes two environmental variables have been set:

numlabs:  full path to root of github numeric checkout

  i.e.

  export numlabs=/Users/phil/repos/numeric
 
numdocs:  full path to root of github numeric_docs checkout

 i.e.

  export numdocs=/Usres/phil/repos/numeric_docs

finds all ipython notebooks in numlabs matching the regular expression
01-*ipynb and records their path and modification time

finds the corresponding paths to the html and pdf versions of the
notebooks in $numdocs/pdf_files and $numdocs/html_files and
compares modification times with ipynb source -- if source is newer,
appends to list for recompilation



"""
from bookbook.html import convert as convert_html
from bookbook.latex import combine_and_convert as convert_latex
import os
from tempfile import TemporaryDirectory
from pathlib import Path
import re
import subprocess



def build_pages(notebook: dict):
    """
    given a notebook dictionary create a temporary directory
    in the parent folder of the ipynb file and build latex and html versions
    of the notebook
    """
    lab_ipynb=notebook['lab_ipynb']
    build_path=lab_ipynb.parent
    html_path=str(notebook['html_path'])
    html_file=notebook['html_path'].name
    pdf_path=str(notebook['pdf_path'])
    pdf_file=notebook['pdf_path'].name
    #
    # make sure we wind up back in the calling directory if something goes wrong
    #
    return_dir=os.getcwd()
    try:
        with TemporaryDirectory(dir=build_path) as td:
            os.chdir(td)
            print('here is cwd: ',os.getcwd())
            convert_html(lab_ipynb,td)
            print(f'here is {build_path} and {td}')
            output_name=Path(td) / lab_ipynb.name
            print('output_name: ',output_name)
            convert_latex(build_path,output_name)
            print(f"converting {notebook['lab_ipynb']} in {td}")
            latex_file = output_name.with_suffix('.tex')
            out=subprocess.run(['latexmk','-pdf',str(latex_file)],
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=subprocess.run(['rsync','-av',html_file,html_path],
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print(out.stdout)
            out=subprocess.run(['rsync','-av',pdf_file,pdf_path],
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print(out.stdout)
            # out=subprocess.run(['ls','-lRt','.'],
            #         stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            # output=out.stdout.decode('utf-8')
            # for item in output.split('\n'):
            #     print(item)
            # out=subprocess.run(['latexmk','-pdf','templatex.tex'],
            #        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    finally:
        os.chdir(return_dir)

if __name__ == "__main__":
    numlabs=Path(os.environ['numlabs']).resolve()
    numdocs=Path(os.environ['numdocs']).resolve()
    the_notebooks=list(numlabs.glob('**/*.ipynb'))
    match_notebook=re.compile('01.*ipynb')
    notebook_dict={}

    for item in the_notebooks:
        if match_notebook.match(item.name):
            if str(item).find('checkpoints') > 0:
                continue
            html_path=(numdocs / Path('html_files') / item.name).with_suffix('.html')
            pdf_path=(numdocs / Path('pdf_files') / item.name).with_suffix('.pdf')
            try:
                html_mtime=html_path.stat().st_mtime
            except FileNotFoundError:
                html_mtime=-1
            notebook_dict[item]=dict(lab_ipynb=item,lab_mtime=item.stat().st_mtime,
                                     html_path=html_path,
                                     pdf_path=pdf_path,html_mtime=html_mtime)

    for key,notebook in notebook_dict.items():
        print('notebook and html_mtime: ',key,notebook['html_mtime'])
        if notebook['lab_mtime'] > notebook['html_mtime']:
            build_pages(notebook)
    
    
        
# notebook_list = list(notebook_dict.keys())
# notebook_list.sort()
# print(notebook_list)

# for the_notebook in notebook_list:
#     build_pages(the_notebook)
    
# print(notebook_dict)


    
