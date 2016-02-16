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