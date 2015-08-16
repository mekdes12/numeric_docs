.. _lab5 extra:

Extra lab 5 problem -- due Friday Nov. 4
________________________________________


- Solve the steady state temperature problem of 
  `Mini Project 1 (pdf) <../../../labs/newminiprojectv2.pdf>`_

  .. math::

     A_{max}, & d < h \\ 

     A_{depth} + \left[A_{max}-A_{depth}-A_{dip}(d-h)\right] \exp \left[-0.5(d-h)\right], & d > h. \\

     \frac{\partial T}{\partial t} =& 0 =  \frac {\partial }{\partial d} 
        \left(A_h \frac {\partial T}{\partial d} \right) - 
        \frac{ 1} {c_p} \frac {\partial I}{\partial d}


  using the standard ode integrator for Python (scipy.integrate.odeint)
  or matlab (ode45)

- Use an exact form for :math:`\frac{\partial^2T}{\partial d^2}`.  
  You'll need to chain
  rule the first term in equation (3), which requires
  :math:`\frac{\partial A_h}{\partial d}`.  I will provide matlab
  and python versions of this function, along with :math:`A_h(d)` and
  :math:`\frac{\partial I(d)}{\partial d}`, and values for
  all the coefficients.

- Initial conditions:  :math:`T(d=0) = -1\ ^\circ C`,
  :math:`T^\prime(d=0) = 0.00105563 ^\circ C/m`

- As a side effect, have your derivative function save the temperature
  and height for each time it is called

- Turn in a script which makes a plot of temperature as a function of depth,
  along with the :math:`T,depth` values returned by the ode integrator
  overlayed as dots or crosses (identified in your legend)
  Ask the integrator for 10 meter spacing between
  0-50 meters, and 50 meter spacing below 50 meters.

- Compare the solution you get using the odesolver with the fixed-grid
  solution you obtained for the miniproject.  Are the two techniques
  solving the same problem?  

Matlab and python files
-----------------------

Click on these to save

- `mini1_data.txt <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/mini1_data.txt>`_
  contains three columns with (z,Temp, Ah) from the solution with these values
  for the various parameters::

    co.Amax = 1e-2
    co.Adepth = 1e-4
    co.Adip = 1.5e-3
    co.h = 10
    co.beta=0.5
    co.alpha=0.1
    co.cp=4.e6
    co.I0=100.
    co.albedo=0.1

- `plot_derivs.m <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/plot_derivs.m>`_ and
  `plot_derivs.py <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/plot_derivs.py>`_
  are matlab and python programs that plot the analytic formulas for :math:`A_h` and :math:`dA_h/dz`
  and compare  :math:`dA_h/dz` with a finite difference version to show that I've actually
  done the derivative correctly


- `test_solve.m <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/test_solve.m>`_ and
  `test_solve.py <http://clouds.eos.ubc.ca/~phil/numeric/labs/lab5/lab5_files/test_solve.py>`_
  are matlab and python programs that show how to use the built-in matlab and python
  ode integrators to solve a second-order ode and write the intermediate results to a
  file, with test plots showing the guesses the integrators took.

- Your script should use the Ah and dAh/dz routines from plot_derivs and the structure of
  test_solve to setup and solve the miniproject equation.  I found a good fit to the
  answer by starting with an initial temperature of -1 degC and an initial dT/dz=0.00105563 deg C/m
