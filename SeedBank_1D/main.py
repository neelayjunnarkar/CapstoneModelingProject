from tools import *

K  = 1.0  #Population Carrying Capacity
gm = 0.04 #Maximum Growth Rate
l  = 0.6  #Fraction of plants that live
e  = 5.0    #Number of seeds per plant 
N  = 10.0   #Length of space
T  = 10.0   #Number of generations the program is run for
mig= [1.0/(2.0**(x+1.0)) for x in range(int(N/2))]   #Lookup table of fractions of seeds that go to i dist away from the original cell

def main():
    P = np.arange(N*T).reshape((N, T)) #indices 
    S = np.arange(N*T).reshape((N, T))
    P[:][:]   = 2.0
    P[0][N/2] = 0.01
    S[:][:]   = 0

    SeedsGend = np.arange(N)
    for t in range(0,int(T-1)): #[0, T-2]
        SeedsGend = e*P[t]  
        print SeedsGend    
        
        
main() 