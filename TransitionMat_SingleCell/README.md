# A Seed Bank Model of a Single Cell Plant Population using a Transtion Matrix #

* Models the plant and seed-bank popuulations in a single cell with no migration using a transition matrix
* Survivorship of seeds is 1.0

## Dependencies ##
* python2.7.11
* ipython
* numpy
* matplotlib
 
A simple way to install these is to install Anaconda2

## Running the program ##
`ipython --pylab=tk`

`%run main.py`

## Equation ##
X_t+1 = M*X_t

where:
* X_n is a 2x1 matrix (row x col) which holds seed-bank size and plant population
* M is the 2x2 transition matrix
