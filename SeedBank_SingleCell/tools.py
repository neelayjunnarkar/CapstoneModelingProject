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

#Saves existing data as PNG 
def save_image(name, x, y, xmax, ymax):
    plot = go.Scatter(
        x = x,
        y = y,
        name = name
    )
    
    layout = go.Layout(
        xaxis = dict(
            range = [0, xmax]
        ),
        yaxis = dict(
            range = [0,ymax]
        )
    )

    figure = {
        'data': [plot],
        'layout': layout
    }
    py.image.save_as(figure, "{}{}.png".format(generate_image_id(len(x)-1), name))
    
