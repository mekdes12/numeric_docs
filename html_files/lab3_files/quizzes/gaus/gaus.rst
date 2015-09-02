Solution to Gaussian Elimination
================================

****

****

Given the set of linear equations:

|image0|

| Let's look at the solution graphically first.

| Figure 1:
|  |image1|
|  Figure 2:
|  |image2|
|  Figure 3:
|  |image3|

Figure 1 is the plane of |image4|, Figure 2 is the plane of |image5|,
and Figure 3 is the plane of |image6|.

The final result will be the intersection of the three planes:

|image7|

One way of solving the equations:

#. Divide |image8| by 2; multiply |image9| by 3 and subtract it from
   |image10| to cancel |image11| from |image12|; subtract the new
   |image13| from |image14| to cancel |image15| from |image16|:

   |image17|

#. Divide |image18| by -18; multiply |image19| by 2 and add it to
   |image20| to cancel |image21| from |image22|:

   |image23|

#. Now, solve for |image24|, and substitute it into |image25| to solve
   for |image26|; then substitute |image27| and |image28| into |image29|
   and solve for |image30|:

   |image31|

So, |image32| = -2, |image33| = 9 and |image34| = 3.

Solving the equations in a matrix:

Two main steps are involved in this solution. The Gaussian elimination
is performed first, followed by the Back-substitution:

-  Reducing the matrix with Gaussian elimination

   |image35|

-  Back-substitution

   | Reading from the matrix:

   -  finding |image36|

      |image37|

   -  finding |image38|

      |image39|

   -  finding |image40|

      |image41|

So, |image42| = -2, |image43| = 9 and |image44| = 3. As expected, the
two different methods give the same answer.

| 

--------------

*John M. Stockie
 Fri Sep 8 14:25:44 PDT 1995*

.. |image0| image:: img1.gif
.. |image1| image:: eq1.gif%0A
.. |image2| image:: eq2.gif%0A
.. |image3| image:: eq3.gif%0A
.. |image4| image:: img2.gif
.. |image5| image:: img3.gif
.. |image6| image:: img4.gif
.. |image7| image:: inter.gif%0A
.. |image8| image:: img5.gif
.. |image9| image:: img6.gif
.. |image10| image:: img7.gif
.. |image11| image:: img8.gif
.. |image12| image:: img9.gif
.. |image13| image:: img10.gif
.. |image14| image:: img11.gif
.. |image15| image:: img12.gif
.. |image16| image:: img13.gif
.. |image17| image:: img14.gif
.. |image18| image:: img15.gif
.. |image19| image:: img16.gif
.. |image20| image:: img17.gif
.. |image21| image:: img18.gif
.. |image22| image:: img19.gif
.. |image23| image:: img20.gif
.. |image24| image:: img21.gif
.. |image25| image:: img22.gif
.. |image26| image:: img23.gif
.. |image27| image:: img24.gif
.. |image28| image:: img25.gif
.. |image29| image:: img26.gif
.. |image30| image:: img27.gif
.. |image31| image:: img28.gif
.. |image32| image:: img29.gif
.. |image33| image:: img30.gif
.. |image34| image:: img31.gif
.. |image35| image:: img32.gif
.. |image36| image:: img33.gif
.. |image37| image:: img34.gif
.. |image38| image:: img35.gif
.. |image39| image:: img36.gif
.. |image40| image:: img37.gif
.. |image41| image:: img38.gif
.. |image42| image:: img39.gif
.. |image43| image:: img40.gif
.. |image44| image:: img41.gif
