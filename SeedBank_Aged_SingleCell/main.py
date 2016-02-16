"""
Model of Plant and Aged SeedBank Populations in a Single Cell using a Transition Matrix

author: Neelay Junnarkar
"""

#       S1          S2            P
#     ---                         ---
#  S1 | 0            0            e |
#     |                             |
#  S2 | ss(1-g1)     0            0 |
#     |                             |
#  P  | g1           g2           l |
#     ---                         --- 
#
#  S1: Seed Bank Age 1
#  S2: Seed Bank Age 2
#      Seeds do not pass 2 years in the seed bank
#  P:  Reproductive Plant Population 
#
#  e:  Seeds produced per plant
#  ss: Seed Survivorship
#  g1: Fraction of 1 year old seeds that germinate
#  g2: Fraction of 2 year old seeds that germinate
#  l:  Fraction of plants that do not die each year   



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
print "Dependencies loaded..."

# Number of steps the model will be run for
T = 10

# Seed Survivorship. Fraction of seeds that remain in seed bank that can germinate
ss = 1.0

# Fraction of seeds that become reproductive plants
g1 = 0.024
g2 = 0.020

# Fraction of plants that continue to live
l = .9

# Seeds produced per plant
e = .2

# Transition Matrix
M = np.arange(float(3.0*3.0)).reshape((float(3.0),float(3.0)))

# Matrix holding seedbank and plant population data
# Row 0 is seedbank data
# Row 1 is plant population data
X = np.arange(float(3.0*T)).reshape(3.0,float(T))

# Transition Matrix values
M[:,:] = 0.0
M[0] = [0,         0,  e]
M[1] = [ss*(1-g1), 0,  0]
M[2] = [g1,        g2, l]
print M

# Initial population values
X[:,:] = 0.0
X[0,0] = 10.5
X[1,0] = 10.5
X[2,0] = 10.5 

# Set up plotting tools
fig = plt.figure()
axesp  = fig.add_subplot(311, xlim=(0.0,T), ylim=(0.0, 40), title='Plant Population')
axess1 = fig.add_subplot(312, xlim=(0.0,T), ylim=(0.0, 40), title='SeedBank Year 1 Size')
axess2 = fig.add_subplot(313, xlim=(0.0,T), ylim=(0.0, 40), title='SeedBank Year 2 Size')
seedbank1, = axess1.plot(range(T), X[0])
seedbank2, = axess2.plot(range(T), X[1])
plantpop,  = axesp.plot(range(T), X[2])

def update_data(t):

def update_graph(t):

def init_graph():

def main():

main()