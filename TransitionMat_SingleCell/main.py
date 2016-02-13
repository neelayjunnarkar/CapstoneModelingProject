from tools import *

rm = 0.2 # Maximum growth rate
K  = 1.0 # Carrying Capacity
M = np.arange(float(1)).reshape((float(1), float(1)))
M[:] = 0.0 
T = 30

def main():
    P = np.arange(float(1*T)).reshape((float(1),float(T)))
    P[:,:] = 0.0
    P[0,0] = 0.2

    for t in range(0,T-1):
        M[0,0] = 1.0+rm*(1-(P[0,t]/K))
        P[0,t+1] = np.matmul(M, [P[0,t]])
    print P
    for t in range(0, T-1):
        print "Saving Time-Step {}".format(t)
        save_image("population", range(0, t+2), P[0, :t+2], T, 1.1)
main()
