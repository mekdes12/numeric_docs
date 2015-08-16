.. toctree::
   :hidden:

   lab5_extra

Lab/course information
======================

Course syllabus with due dates
______________________________

- `A409 syllabus 2011 <http://clouds.eos.ubc.ca/~phil/numeric/course/syllabus11.pdf>`_

- `E511 syllabus 2011 <http://clouds.eos.ubc.ca/~phil/numeric/course/gradsyllabus11.pdf>`_


Resources
_________


Free online: Numerical Recipes (Advanced)
-----------------------------------------

-  `C and Fortran chapters <http://www.nr.com/oldverswitcher.html>`_

Matlab resources (lab 3 and beyond)
-----------------------------------

- `EOS Matlab page <http://clouds.eos.ubc.ca/~phil/courses/matlab>`_

- To customize matlab in the EOS computer lab, download `startubc.m <http://clouds.eos.ubc.ca/~phil/numeric/course/startubc.m>`_ and put it in your z:directory.
  You can then edit it to add commands like
  "addpath(z:\\a409\\lab2')" that will be executed each time you
  start Matlab


Python resources
----------------

- `Links to python tutorials <python.html>`_


Lab 1: Introduction to Numerical Methods
________________________________________

Click on `lab1.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab1/lab1.pdf>`_ for the lab 1
instructions. Read the lab and hand in answers to the problems in
`assignment 1 <http://clouds.eos.ubc.ca/~phil/numeric/course/assignment1.pdf>`_.
(Because of internet security holes, the interactive examples in
the labs have had to be disabled. However we have rewritten many of
them in octave/matlab/html so you can run them locally. Click
`Readme_lab1.pdf <http://clouds.eos.ubc.ca/~phil/numeric/course/Readme_lab1.pdf>`_ for the
instructions and `lab1_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab1/lab1_files>`_ to download the
files.)

Lab 2: Introduction to Numerical Methods, Part II
_________________________________________________

Download `lab2.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab2/lab2.pdf>`_.
As for lab 1, you'll need to run these examples locally. Click on 
`Readme_lab2.pdf <http://clouds.eos.ubc.ca/~phil/numeric/course/Readme_lab2.pdf>`_ for the
instructions and `lab2_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab2/lab2_files>`_ to download the
files.
Do the following questions:

-  A409: 1a, 1b, 2a, 2b, 3, 4, 5
-  E511: 1a, 1b, 2a, 2b, 3, 4, 5

Lab 3: Linear Algebra
_____________________

Download `lab3.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab3/lab3.pdf>`_
Click on `Readme_lab3.pdf <http://clouds.eos.ubc.ca/~phil/numeric/course/Readme_lab3.pdf>`_ for the
extra instructions and `lab3_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab3/lab3_files>`_ to
download the files.

Read the lab and hand in answers to the problems in
`assignment 3 <http://clouds.eos.ubc.ca/~phil/numeric/course/numeric_assignment3_2009.pdf>`_.

Mini-project I
--------------

- `Mini Project 1 (pdf) <http://clouds.eos.ubc.ca/~phil/numeric/labs/newminiprojectv2.pdf>`_

Lab 4: ODE Lab - Runge Kutta methods
____________________________________

`lab4.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab4/lab4.pdf>`_

Click on `Readme_lab4.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab4/lab4_files/Readme_lab4.pdf>`_ for the
extra instructions and `lab4_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab4/lab4_files>`_ to
download the files.
Do the following questions:

-  E511: 2.1, 3.1, 5, 7.2, 7.3, 7.5
-  A409: 2.1, 3.1, 5, 7.2, 7.3

Lab 4 hints:

1) Question 5 is asking you to find the exact (analytic) solution to the
   equation defined in *lab4_files/matlab/example1/derivs4.m* or
   *lab4_files/python/example1/lab4_functions.py*.  Specifically, you need
   to turn this code::

     f=ones([1,2]); %create a 1 x 2 element vector to hold the derivitive
     f(1)=y(2);
     f(2)= -1.*coeff.c1*y(2) - coeff.c2*y(1);

   into a 2nd order ODE and solve it as in Math 215.  To do this recognize
   that you are solving two first order odes:


   .. math::

           \frac{dy}{dt} &= z \\

           \frac{dz}{dt} &= -c_1 z - c_2 y

   Take the derivitive of the first eqn wrt t, and insert it into
   the second equation to get a single 2nd order differential equation in y
   with a simple analytic solution.  It's that solution that you
   are asked to compare with the output you get from the midpoint method

2) Question 7 is asking you to compare the midpoint and Heun's method
   on the dampled oscillator problem -- see if you can figure out how
   to plot the solutions
   on top of each other on the same graph or subtract them to get
   a detailed look at the differences.


Lab 5: ODE Lab - Daisy World
____________________________

Click on `Readme_lab5.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/Readme_lab5.pdf>`_ for the
extra instructions and download
`current matlab, octave and python zip files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files>`_. 
(Check the date to see whether there are bug fixes).  The lab itself
is: `lab5.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5.pdf>`_


It may also help to read the section on adaptive Runge Kutta in
`Numerical Recipes <http://clouds.eos.ubc.ca/~phil/readings/adaptive_rk.pdf>`_
Reading this pdf requires a special acrobat add-on which you can download
from `numerical recipes plug-in <http://www.nr.com/plugin/plugin_install.html>`_.
Alternatively, I have placed a scanned version here called
`adapt_ode.pdf <http://clouds.eos.ubc.ca/~phil/readings/adapt_ode.pdf>`_

Do the following questions:

-  E511: 5, 6.2, 6.3, 8
-  A409:4.1, 4.2, 6.1, 6.2, 6.3

- A409:  do this :ref:`lab5 extra`


-  E511 ODE track: do
   `rabbits and foxes <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/Readme_lab5_extra.txt>`_

Mini-project 2
--------------

Click `Readme_mini2.txt <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/Readme_mini2.txt>`_ for
instructions for Miniproject 2

Lab 6: ODE Lab - Lorenz Equations (E511 ODE track only)
_______________________________________________________

`lab6.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab6/lab6.pdf>`_

Octave and Matlab programs to integrate the Lorentz equations are
`lab6_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab6/lab6_files>`_ (note that all files are
available as lab6\_matlab.zip or lab6\_octave.zip)

Problems for this lab: do problems 4, 5, 6

`Quiz 8 solution <quiz8_sol.pdf>`_

Lab 7: PDE Lab - Solving PDEs using an explicit, finite difference method
_________________________________________________________________________

`lab7.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7.pdf>`_

Do the following questions:

-  A409: 1, 2a and 4
-  E511: 2b, 4 and 5

For E511 PDE track download

-  `lab7b.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7b.pdf>`_
-  `matlab7b.zip <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7_files/matlab7b.zip>`_

Click `Readme_lab7a.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7_files/lab7a/Readme_lab7a.pdf>`_ for
the extra instructions and `lab7a <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7_files/lab7a>`_
for the extra files for part a (note that all files are available
as lab7a.zip).

Click `Readme_lab7b.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7_files/lab7b/Readme_lab7b.pdf>`_ for
the extra instructions and `lab7b <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab7/lab7_files/lab7b/>`_
for the extra files for part b (note that all files are available
as lab7b.zip)

Lab 8: PDE Lab - Solution of the quasi-geostrophic equations using an implicit scheme
_____________________________________________________________________________________

- `Lab 8 writeup <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab8/lab8.pdf>`_

- `Lab 8 exercises (2009) <http://clouds.eos.ubc.ca/~phil/numeric/course/numeric_assignment8_2009.pdf>`_.

Click `Readme_lab8.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab8/lab8_files/extras8.pdf>`_ for the
extra instructions and `here <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab8/lab8_files>`_ for the
files (note that all matlab files are available in this directory as
`lab8_matlab.zip <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab8/lab8_files/lab8_matlab.zip>`_)

Lab 9: Fourier transforms
_________________________

`lab9.pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab9/fft.pdf>`_

`Numerical recipes on ffts <http://clouds.eos.ubc.ca/~phil/readings/numerical_recipes_fft.pdf>`_

Vertical velocity and temperature data file `miami.mat <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab9/lab9_files>`_

Matlab and python code `lab9_files <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab9/lab9_files>`_

Lab 10: Advection schemes
_________________________

`lab10 pdf <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab10/source/lab10.pdf>`_

Octave programs for lab 10 can be downloaded
`lab10 octave <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab10/octave>`_ or
`lab10 matlab <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab10/matlab>`_

--------------

e-mail: `paustin@eos.ubc.ca <mailto:paustin@eos.ubc.ca>`_
