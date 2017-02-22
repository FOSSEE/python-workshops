# Introductory Scientific Computing with Python

This is an entirely hands-on workshop. At the end of this workshop, attendees
should be able to use the basic tools and libraries for Python-based
scientific computing. We imagine that an undergraduate/graduate
engineering/science student would be able to *start* doing their basic
computing tasks using Python.

The course features multiple simple quizzes that students take online. Based
on the performance in these quizzes students are given grades and a
certificate.


## Intended audience and pre-requisites

This course is designed to be taken by folks who do not have any programming
experience. The students should be comfortable using a computer and editing
text files.

Prior experience with Scilab/Matlab/octave or similar tools would be useful
but not necessary.

For those of you who do not have much experience using a keyboard to type or do
not know touch typing, it would be a good idea to practice typing using online
typing tutors.  Here is a good one:

https://www.speedtypingonline.com/typing-tutor

Just practice and go through the default lessons and learn the basic keys.  The
more you practice the better you become.  If you are not good at typing quickly,
you might benefit from a few hours of practice.  Try to log two to four hours on
this and you will find that your typing speed improves significantly.


## Software and hardware requirements:

A laptop or reasonably configured desktop is recommended since this will be a
hands-on session.

The following packages need to be installed:

- Python (2.x or 3.x)
- IPython/Jupyter
- NumPy
- SciPy
- Matplotlib
- Optionally install Mayavi.

On Linux, Windows and Mac OS X it is easiest to install these by installing
the Enthought Canopy. Download the Canopy Python distribution for your OS and
architecture from here: https://store.enthought.com/downloads.

You could also use Anaconda or Conda along with the Spyder editor to obtain
the requirements.

On many Linux distributions, these packages are easy to install.


## Detailed outline

The session is entirely hands-on. We focus on common tasks and introduce the
Python language in the context of these common tasks. Here is an outline
of what is covered:

- Introduction to Python and some preliminaries.

- Getting started with IPython and creating basic plots with `pylab`.
  - Using IPython effectively, reading documentation interactively.
  - Basic plots.
  - Decorating plots with labels, legends, annotation, and titles.
  - Multiple plots and separate figures.
  - Saving plots.

- Saving Python scripts and running them using IPython and Python.
  - Using `%hist` and `%save`
  - Creating new Python scripts on an editor.
  - Running scripts in IPython using `%run`.
  - Running scripts from the terminal with `python`.

- Creating and using lists, list slicing, list operations.
  - Creating data and storing them in lists.
  - Plotting data in lists.
  - Initializing and accessing list elements with indexing
  - List slicing, striding, and list operations
  - Looping over a list with `for`.

- Defining functions in Python.
  - Functions accepting arguments and returning values.

- Timing operations using IPython's `%timeit` and `%time` magic.

- NumPy array basics:
  - Importing numpy.
  - Basic array attributes and operations.
  - 1-D and multi-dimensional arrays.
  - Array slicing and striding.
  - Other array creation functions.
  - Basic array math.
  - Reading data files with `loadtxt`.
  - Exercise on plotting data from a file.

- More on NumPy.
  - Creating matrices using numpy arrays.
  - Special kinds of matrices, `ones`, `identity` etc.
  - Accessing elements, accessing rows and columns.
  - Setting elements, setting rows and columns.
  - Multi-dimensional slicing and striding.

- Elementary image processing using numpy arrays.
  - Reading an image and matrix as a numpy array.
  - Viewing an image/matrix.
  - Basic cropping, sub-sampling images.

- More matrix operations.
  - Transposition.
  - Elementwise addition/multiplication.
  - Matrix multiplication with `numpy.dot`.
  - Inverse, determinant, sum of elements.
  - Computing norms, eigenvalues, and eigenvectors.
  - Computing the singular value decomposition.

- Performing a least squares fit for some experimental data.
  - Read data from a file.
  - Perform a least square fit from first principles.

- Introduction to random number generation with `numpy.random`.

- Introduction to Jupyter/IPython notebooks.
  - Starting up the notebook.
  - Using `%pylab` and `%matplotlib`.
  - A sample notebook with a demonstration of images, equations, code, and
    simple widgets.

The above are covered first, additional material is also made available to
users that they can see at their leisure. These are optional but students are
suggested to go over the material on their own.

- Introduction to the SciPy package. (52 minutes)

  - Solving a system of linear equations.
  - Finding the roots of a polynomial using `numpy.roots`.
  - Finding the roots of non-polynomial equations using scipy's `fsolve`.
  - Numerical integration of Ordinary Differential Equations (ODES).
    - Example of a 1D ODE.
    - Example of a coupled 2D ODE or a second order DE.
  - Using scipy's `fft` module for basic signal processing
    - Finding the FFT and inverse FFT.
    - Simple noise filtering using `scipy.signal`.

- Exercises: (65 minutes)
  - We solve 5 different problems using the tools we have learned.
  - Users are given time to solve the problem.
  - The solution is shown and explained before the next problem.

- Simple 3D plots with Mayavi's `mayavi.mlab`. (50 minutes)
  - Introduction to Mayavi.
  - Getting started with `mlab`
    - Using `mlab` in a console and in an IPython notebook.
  - Basic plotting with Mayavi
  - 0D data, 1D data, 2D data, and 3D data.
  - Simple scalar and vector plots.
  - Utility functions to annotate the plot and save images.


Session wise slide breakup:

1. intro.pdf
2. prelims.pdf
3. ipython_plotting.pdf
4. saving_scripts.pdf
5. lists_arrays.pdf
6. numpy.pdf
7. more_numpy.pdf
8. scipy.pdf
9. exercises.pdf
10. notebook.pdf
11. mlab.pdf
