from tools import *

K  = 1.0  #Population Carrying Capacity
gm = 0.04 #Maximum Growth Rate
l  = 0.6  #Fraction of plants that live
e  = 5.0    #Number of seeds per plant 
N  = 10.0   #Length of space
T  = 10.0   #Number of generations the program is run for
#mig= [1.0/(2.0**(x+1.0)) for x in range(int(N))]   #Lookup table of fractions of seeds that go to i dist away from the original cell

mig = np.arange(N*N).reshape((N, N)) #Matrix Lookup table for migration of seeds
                                      #row i * InitialSeeds gives final seeds in cell i, where i is in range [0,N-1]
#Generate mig matrix
for i in range(0, int(N)):  #i is row, but index i represents cell i
    for c in range(0, int(N)): #c is cell on the column
        d = np.abs(c-i) #d is dist from cell c to cell i
        mig[i][c] = 2.0**(-1-d)

#Pt is Population of cells at time t
#g returns growth of cells Pt
def g(Pt):
    return gm*(1-(1/K)*Pt)
    
def main():
    P = np.arange(N*T).reshape((N, T)) #indices 
    S = np.arange(N*T).reshape((N, T))
    P[:][:]   = 2.0
    P[0][N/2] = 0.01
    S[:][:]   = 0

    
    for t in range(0,int(T-1)): #[0, T-2]
        SeedsInit = e*P[t] #Seeds produced in each cell
        SeedsFinal = np.matmul(mig, SeedsInit) #Seeds in each cell after dispersal
        print "SeedsFinal: {}".format(SeedsFinal)
        
        
        
        
main() 