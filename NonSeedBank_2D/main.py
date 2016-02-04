#creates and animates heatmaps
import plotly.plotly as py
import plotly.graph_objs as go 
import plotly.tools as tls
import numpy as np
import time
from subprocess import call

def num_digits(n):
    c = 1
    while (n/10 != 0):
        n /= 10
        c += 1
    return c;
    
def generate_image_id(n): #Used to identify images created with an ID
    return "{}{}".format("0"*(3-num_digits(n)),n)
    
stream_id = 'd33zwbnu9o'

colorScale = [
    [0.0, "rgb(165,0,38)"],
    [0.1111111111111111, "rgb(215,48,39)"],
    [0.3333333333333333, "rgb(253,174,97)"],
    [0.4444444444444444, "rgb(254,224,144)"],
    [0.2222222222222222, "rgb(244,109,67)"],
    [0.5555555555555556, "rgb(224,243,248)"],
    [0.6666666666666666, "rgb(171,217,233)"],
    [0.7777777777777778, "rgb(116,173,209)"],
    [0.8888888888888888, "rgb(69,117,180)"],
    [1.0, "rgb(49,54,149)"]
]


K= 1.0 #carrying capacity
g_max = 0.3 #maximum growth rate
f_mig = 0.9 #fraction that migrates out of cell
N = 100.0 #side length of spatial grid
T = 50.0 #number of steps
P = np.arange(N*N).reshape(N,N)
P[:] = 0.0 #set everything to 0

P[4][:] = 0.0010 #initial spot of population

M = np.arange(N*N).reshape(N,N)
M[:] = 0.0

mpts1 = []
for x in range(1, int(N)):
    mpts1.append([x])
for y in range(0, int(N-1)):
    mpts1[y].append(y)
mpts2 = []
for x in range(0, int(N-1)):
   mpts2.append([x])
for y in range(1, int(N)):
    mpts2[y-1].append(y)
    
for (x, y) in mpts1:
    M[x][y] = 1.0 
for (x, y) in mpts2:
    M[x][y] = 1.0
M[int(N-1)][0] = 1.0
M[0][int(N-1)] = 1.0

heatmap = go.Heatmap(
    z=P, 
    stream=dict(token=stream_id), 
    colorscale=colorScale,
    zmin = 0.0,
    zmax = 1.0
)
figure = {
    'data': [heatmap]
}

# plot_data = go.Data([heatmap])
# py.plot(plot_data)
# time.sleep(5) # for website to load
# s = py.Stream(stream_id)
# s.open()
# print "stream opened"

for t in range(0, int(T-1)): #range is [x,y)
    K_b = P*(g_max-(g_max/K)*P)
    K_a = (1-f_mig)*K_b + np.matmul(K_b, f_mig/4.0*M) + np.matmul(f_mig/4.0*M, K_b) 
    P += K_a
    # figure = {
    #     'data': [heatmap]
    #     # 'data': [{
    #     #     'z': P,
    #     #     'type': 'heatmap',
    #     #     'colorscale': colorScale,
    #     #     'zmin': 0.0,
    #     #     'zmax': 1.0
    #     # }]
    # }
   
    py.image.save_as(figure, "{}img.png".format(generate_image_id(t)))
    print "{}".format(t)
    # s.write(dict(z=P, type='heatmap',colorscale=colorScale,zmin=0.0,zmax=1.0))
    # time.sleep(.05)
    
# s.close()
# print "stream closed" 

# call(['C:\imagemagick\convert.exe','-delay','10','-loop','0','*.png','heatmapanimation.gif'])