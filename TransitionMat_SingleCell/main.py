import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
print "Dependencies loaded..."

T = 100

gm = 0.94
l = 0.9

M = np.arange(float(2.0*2.0)).reshape((float(2.0),float(2.0)))
X = np.arange(float(2.0*T)).reshape(2.0,float(T))
M[:,:] = 0.0
M[0,0] = 0
M[0,1] = 1-l
M[1,0] = gm
M[1,1] = l

X[:,:] = 0.0
X[0,0] = 0
X[1,0] = 2
fig = plt.figure()
axess = fig.add_subplot(211, xlim=(0.0,T), ylim=(0.0, 40))
axesp = fig.add_subplot(212, xlim=(0.0,T), ylim=(0.0,40))

seedbank, = axess.plot(range(T), X[0])
plantpop, = axesp.plot(range(T), X[1])

def update_data(t):
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
    print "Updating graph..."
    update_data(t)
    seedbank.set_data(range(t+1), X[0,:t+1])
    plantpop.set_data(range(t+1), X[1,:t+1])
    return seedbank,plantpop

def init_graph():
    seedbank.set_data([], [])
    plantpop.set_data([],[])
    return seedbank, plantpop

def main():
    print "Beginning animation..."
    a = anim.FuncAnimation(fig, update_graph, frames=range(T-1), repeat=False, blit=True, interval=10) 
    a.save("seedbank_singlecell_transmat.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()
    print "Showing animation..."
main()
