.. toctree::
   :maxdepth: 1


Getting started 
---------------

#. Find the name of your home directory

   On windows:

   #. start a cmd shell by typing "cmd" in the windows search bar and executing the
      dos command prompt

   #. Note the location that is listed when you type

      echo %userprofile%

      in the command window

   On macs:

#. Start a terminal by typing terminal in spotlight

   #. Note the location that is listed when you type

      echo $HOME

#. Install Miniconda Python version 3.6 from https://conda.io/miniconda.html
   into a a folder called mini36 in your home directory.   When prompted, choose to install for just yourself, but make miniconda python the default python

#. To see if your installation is working, start a terminal and type

   where python  (on windows)

   or

   which python (on macs)

   You should see that mini36 python is the version that is found on your path

#. Install the git version control package (which we will learn more about later).  To do this, type

   conda install git

   at a prompt and answer yes to permit the install

#.  Clone the course software into a directory of your choosing.  Create a folder somewhere under your home directory and cd into that folder.  Then type the following at the prompt:

        git clone https://github.com/phaustin/numeric.git

#.  cd into the numeric folder and install the course software by typing (note the double minus sign in front of the e):

        pip install -e .

#.  cd into the numeric/utilities folder and install the required python packages by typing

       conda install --file class_specs.txt

#.  If the packages have installed correctly then typing

       jupyter notebook

    at a prompt should launch jupyter.
              
Books and tutorials
-------------------

-  Jake Vanderplas' [Whirlwind tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython/blob/f40b435dea823ad5f094d48d158cc8b8f282e9d5/Index.ipynb) is available both as a set of notebooks which you can clone from github or as a free ebook: http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp

- A Springer ebook from the UBC library:  [Numerical Python](https://login.ezproxy.library.ubc.ca/login?qurl=https%3a%2f%2flink.springer.com%2fopenurl%3fgenre%3dbook%26isbn%3d978-1-4842-0554-9)
   
- Two texts that are available as a set of notebooks:   

  - https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering   

  - https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb
     
-  Our version of David Pine's Introduction to Python:  http://clouds.eos.ubc.ca/~phil/djpine_python/
   
- My favorite O'Reilly book is:

  - `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_

- Some other resources:

  - If you know Matlab, there is `Numpy for Maltab users <http://wiki.scipy.org/NumPy_for_Matlab_Users>`_
  
  - `Numpy beginners guide <http://www.packtpub.com/numpy-mathematical-2e-beginners-guide/book>`_

  - `Learning Ipython <http://www.packtpub.com/learning-ipython-for-interactive-computing-and-data-visualization/book>`_

  - `The official Python tutorial <http://docs.python.org/tut/tut.html>`_

  - `Numpy cookbook <http://www.packtpub.com/numpy-for-python-cookbook/book>`_





