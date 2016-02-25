"""
Model of Plant dispersion and growth in 1d space
    Non-aged seed-bank
    Uses transition matrix for cell update
    Migration matrix for migration

author: Neelay Junnarkar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
print "Dependencies loaded..."

STEP_OUTPUT = True
print "Output on each step is {}".format("enabled" if STEP_OUTPUT else "disabled")

# Transition Matrix--calculates size of population at next data step
#      S       P
#    ---       ---
# S  | ss(1-g) e |
#    |           |
# P  | g       l |
#    ---       ---
# S: Seed Bank
# P: Plant Population
#
# ss: Seed Survivorship
# g:  Germination fraction of seeds
# e:  Seeds per plant
# l:  Fraction of plants that live to next generation

# Number of steps the model will be run for
T = 4

# Number of cells
N = 3

# Seed Survivorship. Fraction of seeds that remain in seed bank that can germinate
ss = 0.7

# Fraction of seeds that become reproductive plants
g = 0.024

# Fraction of plants that continue to live
l = 0

# Seeds produced per plant
e = 27

# Transition Matrix
M = np.arange(float(2.0*2.0)).reshape((float(2.0),float(2.0)))

# Matrix holding seedbank and plant population data
# [time, cell data, cell]
# time:      indices[0,T-1]
# cell data: indices[0,1]
#   0: Seed Bank
#   1: Plant Population
# cell:      indices[0,N-1]
X = np.arange(float(T*N*2.0)).reshape((float(T),2.0,float(N)))

# Transition Matrix values
M[:,:] = 0.0
M[0] = [ss*(1-g), e]
M[1] = [g,        l]
# print M

# Initial population values
X[:,:,:] = 0
X[0,0,1] = 23  # Set seedbank of 2nd cell at time 0
X[0,1,1] = 0.5 # Set population size of 2nd cell at time 0
  
# Set up plotting tools
pop_maxy = 11
seed_maxy = 300
fig = plt.figure()
axesp = fig.add_subplot(211, xlim=(0.0,N), ylim=(0.0, pop_maxy), title='Plant Population')
axess = fig.add_subplot(212, xlim=(0.0,N), ylim=(0.0, seed_maxy), title='Seed Bank Size' )
seedbank, = axess.plot(range(N), X[0,0])
plantpop, = axesp.plot(range(N), X[0,1])

def update_data(t):
    """
    Is run each step
    Calculates the seedbank size and plant population in the next step by 
        multiplying M, the transition matrix, by X, the data matrix
    """
    if STEP_OUTPUT:
        print "Updating data..."
    
def update_graph(t):
    """
    Is run each step
    After calculating data by calling update_data, updates the data that will be plotted
    """
    if STEP_OUTPUT:
        print "Updating graph..."
    update_data(t)
    seedbank.set_data(range(t+1), )
    plantpop.set_data(range(t+1), )
    return seedbank, plantpop
    
def init_graph():
    """
    Initializes the plot to nothing
    """
    plantpop.set_data([],[])
    seedbank.set_data([],[])
    return seedbank, plantpop

def main():
    """
    Entry point for the program
    Runs an animation of the model
    This animation is displayed, and also saved to an mp4
    """
    print "Beginning animation..."
    a = anim.FuncAnimation(fig, update_graph, frames=range(T-1), repeat=False, blit=True, interval=10) 
    a.save("seedbank_1d.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    fig.tight_layout()
    fig.show()
    print "Showing animation..."
main()