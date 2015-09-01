.. _assign1:
   
Assignment Set for Laboratory 1
===============================

Here is a pdf copy `assignment1.pdf <pdf_files/assignment1.pdf>`_

**ATSC 409: Hand-in answers to questions 1, 2 and 3.**

**EOSC 511/ATSC 506: Hand-in answers to questions 1, 3 and 4.**

#. Given the following four (x,y) points (-5,-1), (0,0), (5,1), (8,4)
   find the y-value at x=3 using

   #. Linear Interpolation

   #. Cubic Interpolation

#. Given the equation

   .. math:: \frac{dy}{dt} = y(y+t)

   write down

   #. forward Euler difference formula

   #. backward Euler difference formula

   #. centered difference formula

#. The equation

   .. math:: \frac{dy}{dt} + c \frac{dy}{dx} = 0,\ y = \cos(x)\ {at}\ t=0,\ \frac{dy}{dt} = c \sin(x)\ {at}\ t=0

   has a solution :math:`y=\cos(x-ct)`.

   #. Expand both derivatives as centred differences.

   #. Show that the algebraic solution is an exact solution of the
      difference formula if we choose :math:`\Delta x = c \Delta t`.

#. Given

   .. math:: \frac{dy}{dt} = -\alpha y,\ y = 1 \ {at}\ t=0

   #. Show that the forward Euler method gets a smaller answer than the
      backward Euler method for all :math:`t > 0`, provided that
      :math:`0 < \alpha^2 \Delta t^2 < 1`.

   #. Solve the equation analytically.

   #. Show that the forward Euler always under-estimates the answer
      provided that
      :math:`\alpha \Delta t < 1 \ {and}\ \alpha \Delta t \ne 0`.
