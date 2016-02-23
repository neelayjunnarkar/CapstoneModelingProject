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

# Number of steps the model will be run for
T = 100

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
# Row 0 is seedbank data
# Row 1 is plant population data
X = np.arange(float(2.0*T)).reshape(2.0,float(T))

# Transition Matrix values
M[:,:] = 0.0
M[0] = []
M[1] = []
print M

# Initial population values

# Set up plotting tools
pop_maxy = 11
seed_maxy = 300
fig = plt.figure()
axesp = fig.add_subplot(211, xlim=(0.0,T), ylim=(0.0, pop_maxy), title='Plant Population')
axess = fig.add_subplot(212, xlim=(0.0,T), ylim=(0.0, seed_maxy), title='Seed Bank Size' )
seedbank, = axess.plot(range(T), X[0])
plantpop, = axesp.plot(range(T), X[1])

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
def init_graph():
    """
    Initializes the plot to nothing
    """

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