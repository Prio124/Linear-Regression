'''
    File name: main.py
    Author: Giuseppe Priolo
    Date created: 15/09/2020
    Date last modified: 15/09/2020
    Python Version: 3.8.5
'''
#   This program predicts a function which is based on a given data set.
#   The data set format is csv

import pandas
import numpy as np
import matplotlib.pyplot as plt

def create_a_function() :
    #   Create a random functon
    #   Random matrix
    f = np.random.rand(50, 2)
    #Extract the 'x' and 'y' columns
    x = f[:, 0] * 100
    y = f[:, 1] * 100

    return(x,y)

def function_plot(m, q, px, py) :
    x = np.array(range(100))
    for n in x :
        y = m*x + q
    plt.plot(x, y)
    plt.plot(px, py, 'ro')
    plt.show()

def f_prediction(x, y) :
    #All the formulas are in the description
    #f(x) = mx + q

    #Sample Values
    #x = np.array([1,2,3])
    #y=x

    av_x = np.sum(x)/len(x)
    av_y = np.sum(y)/len(y)
    pow_x = x*x
    av_pow_x = np.sum(pow_x)/len(x)
    xy = x * y
    av_xy = np.sum(xy)/len(xy)

    #print(x,y,xy,av_x,av_y,av_pow_x,av_xy)

    m = (av_xy-av_x*av_y)/(av_pow_x-av_x**2)
    q = y[0] - m*x[0]

    return (m,q)


#Test Variables
#f = create_a_function()
#q = f_prediction(f[0], f[1])
#function_plot(q[0], q[1], f[0], f[1])
#function_plot(f[0], f[1])
#csv = {'x': [1,2,3,4],
        'y': [1,2,3,4]
#df = pandas.DataFrame(csv, columns=['x','y'])
