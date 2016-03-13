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

GRAPHING_SCENARIOS = True
if GRAPHING_SCENARIOS == True:
    print "Scenarios will run properly. mp4 will not be saved"
elif GRAPHING_SCENARIOS == False:
    print "SCENARIOS WILL NOT RUN PROPERLY. This is for purposes of saving as mp4 only"
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

# Seed Survivorship. Fraction of seeds that remain in seed bank that can
# germinate
ss = 0.3

# Fraction of seeds that become reproductive plants in the same cell
g = 0.0094

# Fraction of plants that continue to live
l = 0

# Seeds produced per plant
e = 105

# Transition Matrix
# Transition matrix * cell data = next step cell data
M = np.arange(float(N * 2.0 * 2.0)).reshape((float(N), float(2.0), float(2.0)))

# Seed Dispersion Matrix
# Seed Bank Space data * seed dispersion matrix = next seed bank space data
D = np.arange(float(N * N)).reshape((float(N), float(N)))

# Matrix holding seedbank and plant population data
# [time, cell data, cell]
# time:      indices[0,T-1]
# cell data: indices[0,1]
#   0: Seed Bank
#   1: Plant Population
# cell:      indices[0,N-1]
X = np.arange(float(T * N * 2.0)).reshape((float(T), 2.0, float(N)))

# Transition Matrix values
# Transition matrix is the same for all cells (assuming cells are uniform)
# e value is 0 because calculated separately to allow for dispersion of
# seeds that does not disperse seed bank
for matrix in M:
    matrix[:, :] = 0.0
    matrix[0] = [ss * (1 - g), 0.0]
    matrix[1] = [g,        l]

# Seed Bank Dispersion Matrix
D[:, :] = 0.0

# Dispersion Matrix values
dont_disperse = 0.5  # Fraction of seeds that remain in same cell
dispersion_r = 0.5  # Common ratio of geometric sequence by which seed dispersal fraction decreases as distance increases
for src_i in range(0, N):
    cells_to_left = 0#src_i # Number of cells to the left to which seeds will be dispersed
    cells_to_right = N-src_i-1 # Number of cells to the right to which seeds will be dispersed
     
    for dst_i in range(src_i - cells_to_left, src_i + cells_to_right + 1):
        if dst_i < 0 or dst_i >= N:  # Bound-check
            continue
        val = ((1 - dont_disperse) * (1 - dispersion_r)) / (2**(np.abs(src_i - dst_i) - 1)
                                                            * (2 - dispersion_r**cells_to_left - dispersion_r**cells_to_right))
        if np.isfinite(val):
            D[src_i, dst_i] = val
        else:
            D[src_i, dst_i] = 0.0
# Reset values of seeds not dispersing
for src_i in range(0, N):
    D[src_i, src_i] = dont_disperse
print D
# Initial population values
X[:, :, :] = 0
X[0, 0, N / 2] = 2.0   # Set seedbank of 2nd cell at time 0
X[0, 1, N / 2] = 0.1  # Set population size of 2nd cell at time 0

# Copies
M_original = np.copy(M)
D_original = np.copy(D)

# Initial Modifications to Dispersion and transition matrix

# Set up plotting tools
pop_maxy = 200
seed_maxy = 18000
fig = plt.figure()
axesp = fig.add_subplot(211, xlim=(0.0, N - 1),
                        ylim=(0.0, pop_maxy), title='Plant Population')
axess = fig.add_subplot(212, xlim=(0.0, N - 1),
                        ylim=(0.0, seed_maxy), title='Seed Bank Size')
seedbank, = axess.plot(range(N), X[0, 0])
plantpop, = axesp.plot(range(N), X[0, 1])

c1 = 0

print "c: {}".format(c1)

def update_data(t):
    """
    Is run each step
    Calculates the seedbank size and plant population in the next step by
        multiplying M, the transition matrix, by X, the data matrix
    """
    global c1
    global M
    global D
    global M_original
    global D_original

    if STEP_OUTPUT:
        print "[t: {}] Updating data...".format(t)
    # Manual changes in transition matrix and disperion matrix
    if t == 60:
        print "hi"
        c1 = c1+1
#    if t == 60 and c == 2:
#         c = c+1
#         M[N/2+5:, 0] = [ss*(1-g), 0]
#         M[N/2+5:, 1] = [0,        0]
#         D[N/2+5:].fill(0.0)
# 	    print "hi"
# 	print c
#    if t == 68:
# 	c2 = c2+1
#    if t == 68 and c2 == 2:
#        M = np.copy(M_original)
#        D = np.copy(D_original)

    # Calculate Seeds Produced

    # Update each Cell using transition matrix
    # for cell_i in range(0, int(N)):
    #     X_curr = np.mat([[X[t, 0, cell_i]], [X[t, 1, cell_i]]])
    #     X_next = np.matmul(M[cell_i], X_curr)
    #     X[t + 1, 0, cell_i] = X_next[0]
    #     X[t + 1, 1, cell_i] = X_next[1]

    # Migrate Seeds Produced
    # X[t + 1, 0] = np.matmul(X[t + 1, 0], D)
    X[t + 1] = np.transpose([np.matmul(M[c], X[t, :, c]) for c in range(0, int(N))]) + \
        np.matmul(e * np.transpose([[X[t, 1, c], 0]
                                    for c in range(0, int(N))]), D)
    if STEP_OUTPUT:
        print X[t]
    if t == T - 2:
        print "c1: {}".format(c1)
        print "Data Calculation finished"


def update_graph(t):
    """
    Is run each step
    After calculating data by calling update_data, updates the data that will be plotted
    """
    if STEP_OUTPUT:
        print "[t: {}] Updating graph...".format(t)
    update_data(t)
    seedbank.set_data(range(N), X[t, 0])
    plantpop.set_data(range(N), X[t, 1])
    return seedbank, plantpop


def init_graph():
    """
    Initializes the plot to nothing
    """
    plantpop.set_data([], [])
    seedbank.set_data([], [])
    return seedbank, plantpop


def main():
    """
    Entry point for the program
    Runs an animation of the model
    This animation is displayed, and also saved to an mp4
    """
    print "Beginning animation..."
    a = anim.FuncAnimation(fig, update_graph, frames=range(
        T - 1), repeat=False, blit=True, interval=100)
    fig.tight_layout()
    fig.show()
    if !GRAPHING_SCENARIOS:
        a.save("seedbank_1d.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    print "Showing animation..."
    if !GRAPHING_SCENARIOS:
        print "SCENARIOS ARE NOT CORRECT"
main()
