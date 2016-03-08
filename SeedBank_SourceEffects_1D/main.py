"""
Model of Plant dispersion and growth in 1d space
    Non-aged seed-bank
    Uses transition matrix for cell update
    Migration matrix for migration
    Takes into account source effects

author: Neelay Junnarkar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
print "Dependencies loaded..."

STEP_OUTPUT = False
print "Output on each step is {}".format("enabled" if STEP_OUTPUT else "disabled")


#
#
# NEED A WAY TO MODIFY CONDITIONS OF EACH CELL (ENACT SOURCE EFFECTS)
#
#


# Transition Matrix--calculates size of population at next data step
#      S       P
#    ---       ---
# S  | ss(1-g) e |
#    |           |
# P  | g       l |
#    ---       ---
# S:            Seed Bank
# P:            Plant Population
# ss:           Seed Survivorship
# g:            Germination fraction of seeds in same cell
# e:            Seeds per plant
# l:            Fraction of plants that live to next generation

# Number of steps the model will be run for
T = 75

# Number of cells
N = 20

# Seed Survivorship. Fraction of seeds that remain in seed bank that can germinate
ss = 0.3

# Fraction of seeds that become reproductive plants in the same cell
g = 0.024

# Fraction of plants that continue to live
l = 0

# Seeds produced per plant
e = 26

# Transition Matrix
# Transition matrix * cell data = next step cell data
M = np.arange(float(N*2.0*2.0)).reshape((float(N),float(2.0),float(2.0)))

# Seed Dispersion Matrix
# Seed Bank Space data * seed dispersion matrix = next seed bank space data
D = np.arange(float(N*N)).reshape((float(N),float(N)))

# Matrix holding seedbank and plant population data
# [time, cell data, cell]
# time:      indices[0,T-1]
# cell data: indices[0,1]
#   0: Seed Bank
#   1: Plant Population
# cell:      indices[0,N-1]
X = np.arange(float(T*N*2.0)).reshape((float(T),2.0,float(N)))

# Transition Matrix values
# Transition matrix is the same for all cells (assuming cells are uniform)
for matrix in M:
    matrix[:,:] = 0.0
    matrix[0] = [ss*(1-g), e]
    matrix[1] = [g,        l]

# Seed Bank Dispersion Matrix values
# 0.5 seeds stay in cell, and decreases by factor of 1/2 over cells
D[:,:] = 0.0
for row in range(0,N):
    for i in range(0,N):
        val = 2**(-1-(np.abs(row-i)))
        if val > 0.0001 and np.isfinite(val):
            D[row,i] = val
        else:
            D[row,i] = 0.0

# Initial population values
X[:,:,:] = 0
X[0,0,N/2] = 2.0   # Set seedbank of 2nd cell at time 0
X[0,1,N/2] = 0.1 # Set population size of 2nd cell at time 0

# Copies
M_original = np.copy(M) 
D_original = np.copy(D)

# Modifications to Dispersion and transition matrix
# M[N/2+5:, 0] = [ss*(1-g), 0]
# M[N/2+5:, 1] = [0,        0]
# D[N/2+5:].fill(0.0)

# Set up plotting tools
pop_maxy = 800
seed_maxy = 90000
fig = plt.figure()
axesp = fig.add_subplot(211, xlim=(0.0,N-1), ylim=(0.0, pop_maxy), title='Plant Population')
axess = fig.add_subplot(212, xlim=(0.0,N-1), ylim=(0.0, seed_maxy), title='Seed Bank Size' )
seedbank, = axess.plot(range(N), X[0,0])
plantpop, = axesp.plot(range(N), X[0,1])

def update_data(t):
    """
    Is run each step
    Calculates the seedbank size and plant population in the next step by 
        multiplying M, the transition matrix, by X, the data matrix
    """
    global M
    global D
    global M_original
    global D_original
    
    if STEP_OUTPUT:
        print "Updating data..."
        
    # Manual changes in transition matrix and disperion matrix
    if t == 30:
        M[N/2+5:, 0] = [ss*(1-g), 0]
        M[N/2+5:, 1] = [0,        0]
        D[N/2+5:].fill(0.0)
    elif t == 72:
        M = np.copy(M_original)
        D = np.copy(D_original)
    
    # Update each Cell using transition matrix
    for cell_i in range(0, int(N)):
        X_curr = np.mat([[X[t,0,cell_i]],[X[t,1,cell_i]]])
        X_next = np.matmul(M[cell_i], X_curr)
        X[t+1,0,cell_i] = X_next[0]
        X[t+1,1,cell_i] = X_next[1]
    # Migrate seeds
    X[t+1,0] = np.matmul(X[t+1,0],D)
    if STEP_OUTPUT:
        print X[t]
    
def update_graph(t):
    """
    Is run each step
    After calculating data by calling update_data, updates the data that will be plotted
    """
    if STEP_OUTPUT:
        print "Updating graph..."
    update_data(t)
    seedbank.set_data(range(N), X[t,0])
    plantpop.set_data(range(N), X[t,1])
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
