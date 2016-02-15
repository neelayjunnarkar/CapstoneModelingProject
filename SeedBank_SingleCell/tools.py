import plotly.plotly as py
import plotly.graph_objs as go 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def num_digits(n):
    c = 1
    while (n/10 != 0):
        n /= 10
        c += 1
    return c;
    
def generate_image_id(n): #Used to identify images created with an ID
    return "{}{}".format("0"*(3-num_digits(n)),n)

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

    figure = go.Figure(data=[plot], layout=layout)
    py.image.save_as({"data":[plot]}, "{}{}.png".format(generate_image_id(len(x)-1), name))
    
