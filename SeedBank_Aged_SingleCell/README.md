# Aged SeedBank Single Cell Model #

This is a seedbank bank single cell model, where the population produces seeds that may be stored in the seedbank, or may germinate into a plant

Seeds from the seedbank may germinate at a later date, but do not survive past 2 steps

Environmental factors are not included in this model for the likelihood of germination and living rates

## Code ##

main.py contains the model

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

The graphs are saved as an .mp4