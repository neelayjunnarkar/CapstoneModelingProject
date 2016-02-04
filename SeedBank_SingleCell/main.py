from tools import * #All graphing, animation, and math, are in tools.py for simplicity

#To convert images into a gif: 
#   C:\imagemagick\convert.exe -delay 10 -loop 0 *population.png population_plot.gif
#   C:\imagemagick\convert.exe -delay 10 -loop 0 *seedbank.png seedbank_plot.gif
K  = 1.0   #Carrying Capacity
gm = 0.04   #Growth Max
l  = 0.6   #The fraction of plants that live
e  = 5   #Number of seeds per plants
N  = 10    #Side Length of Space
T  = 75    #Number of generations the program is run for

#Pt is Population of plant at time t
def g(Pt):
    return gm*(1-(1/K)*Pt)
    
def main():
    P = np.arange(float(T)) #Plant Population where index is time t
    S = np.arange(float(T)) #Seed Population where index is time t
    
    P[:] = 0.00
    S[:] = 0.00
    P[0] = 0.01

    for t in range(0,T-1):
        P[t+1] = l*P[t] + g(P[t])*S[t] + g(P[t])*e*P[t]
        S[t+1] = S[t] + e*P[t] - g(P[t]) * (S[t] + e * P[t])
        if S[t+1] < 0:
            S[t+1] = 0.0
        if P[t+1] < 0:
            P[t+1] = 0.0
            
    maxy_seed = max(S)
    
    for t in range(0, T-1):
        save_image("population", range(0, t+2), P[:t+2], T, 1)
        save_image("seedbank", range(0, t+2), S[:t+2], T, maxy_seed) 
main()





