from tools import *

# Peculiarity: For this model to reach a steady state, the column
#Constants
T = 50
e = 1 
g = 1 # Fraction of seeds that germinate
M = np.arange(float(4)).reshape((float(2),float(2))) # Transition matrix. Values add to 1 on columns)
M[:,:] = 0.0
M[0,0] = 0
M[0,1] = e
M[1,0] = g
M[1,1] = 0.0 #annuals

def main():
    #Data
    # X[0] = Seeds
    # X[1] = Flowering Plants 
    X = np.arange(float(T*2)).reshape((float(2), float(T)))
    X[:,:] = 0.0
    X[1,0] = .1
    X[0,0] = e*.2

    for t in range(0, T-1):
        X_t = np.arange(float(2*1)).reshape((float(2),float(1)))
        X_t[:,:] = 0.0
        X_t[0,0] = X[0,t]
        X_t[1,0] = X[1,t]
        X_tp1 = np.matmul(M, X_t)
        X[0,t+1] = X_tp1[0,0]
        X[1,t+1] = X_tp1[1,0]
    print X
    for t in range(0, T-1):
        print "Begin T: {}".format(t)
        save_image("population",range(0, t+2), X[1, :t+2], T, max(X[1]))
        save_image("seedbank",  range(0, t+2), X[0, :t+2], T, max(X[0]))
main()
