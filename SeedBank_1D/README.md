# SeedBank One Dimensional #

* Simple migration with 1/2 of seeds staying the cell
    * Fraction of seeds decreases by a factor of 1/2 for each cell distance 
* Single-age seedbank with a fraction of seeds surviving from year to year
* Does not take into accound source effects or path effects

## Code ##

main.py contains the model as well as code for creating graphs and saving as a .mp4


### Dependencies ###
* python2.7.11
* ipython
* numpy
* matplotlib

A simple way to install these is to install Anaconda2

### Running the Program ###
Run ipython from shell using tk as the backend for matplotlib:

```
ipython --pylab=tk
```

Then, in ipython, run the main file:

```
%run main.py
```

## Graphs ##

The graphs are displayed when the program is run, and are saved as a .mp4