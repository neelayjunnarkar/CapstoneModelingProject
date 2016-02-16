"""
Model of Plant and SeedBank Populations in a Single Cell using a Transition Matrix

author: Neelay Junnarkar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
print "Dependencies loaded..."

# Number of steps the model will be run for
T = 100

# Seed Survivorship. Fraction of seeds that remain in seed bank that can germinate
ss = 1.0

# Fraction of seeds that become reproductive plants
gm = 0.024

# Fraction of plants that continue to live
l = .9

# Transition Matrix
M = np.arange(float(2.0*2.0)).reshape((float(2.0),float(2.0)))

# Matrix holding seedbank and plant population data
# Row 0 is seedbank data
# Row 1 is plant population data
X = np.arange(float(2.0*T)).reshape(2.0,float(T))

# Transition Matrix values
M[:,:] = 0.0
M[0,0] = ss*(1-gm)  
M[0,1] = 1-l # Seeds created per plant
M[1,0] = gm
M[1,1] = l

# Initial population values
X[:,:] = 0.0
X[0,0] = 10.5
X[1,0] = 10.5 

# Set up plotting tools
fig = plt.figure()
axess = fig.add_subplot(211, xlim=(0.0,T), ylim=(0.0, 40), title='SeedBank Size')
axesp = fig.add_subplot(212, xlim=(0.0,T), ylim=(0.0,40), title='Plant Population')
seedbank, = axess.plot(range(T), X[0])
plantpop, = axesp.plot(range(T), X[1])

def update_data(t):
    """
        Is run each step
        Calculates the seedbank size and plant population in the next step by multiplying M, the transition matrix, by X, the data matrix
    """
    print "Updating data..."
    X_t = np.arange(2.0*1.0).reshape((float(2.0),float(1.0)))
    X_t[:,:] = 0.0
    X_t[0,0] = X[0,t]
    X_t[1,0] = X[1,t]
    X_tp1 = np.matmul(M, X_t)
    X[0,t+1] = X_tp1[0,0]
    X[1,t+1] = X_tp1[1,0]
    if t == T-2:
        print "Data: {}".format(X[:t+2, :t+2])

def update_graph(t):
    """
        Is run each step
        After calculating data by calling update_data, updates the data that will be plotted
    """
    print "Updating graph..."
    update_data(t)
    seedbank.set_data(range(t+1), X[0,:t+1])
    plantpop.set_data(range(t+1), X[1,:t+1])
    return seedbank,plantpop

def init_graph():
    """
        Initializes the plot to nothing
    """
    seedbank.set_data([], [])
    plantpop.set_data([],[])
    return seedbank, plantpop

def main():
    """
        Entry point for the program
        Runs an animation of the model
        This animation is displayed, and also saved to an mp4
    """
    print "Beginning animation..."
    a = anim.FuncAnimation(fig, update_graph, frames=range(T-1), repeat=False, blit=True, interval=10) 
    a.save("seedbank_singlecell_transmat.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    fig.tight_layout()
    fig.show()
    print "Showing animation..."
main()
