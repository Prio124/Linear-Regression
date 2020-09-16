'''
    File name: main.py
    Author: Giuseppe Priolo
    Date created: 15/09/2020
    Date last modified: 16/09/2020
    Python Version: 3.8.5
'''
#   This program predicts a function which is based on a given data set.
#   The data set format is csv

import pandas
import numpy as np
import matplotlib.pyplot as plt

#Create a class
class linearRegression:

    def insert_data(self, x, y):
        self.x = x
        self.y = y

    def create_a_function(self):
        #   Create a random functon
        #   Random matrix
        f = np.random.rand(100, 2)
        # Extract the 'x' and 'y' columns
        self.x = f[:, 0] * 1000
        self.y = f[:, 1] * 1000

        return (self.x, self.y)

    def f_prediction(self):
        # All the formulas are in the description
        # f(x) = mx + q
        x = self.x
        y = self.y
        # Sample Values
        # x = np.array([1,2,3])
        # y=x

        av_x = np.sum(self.x) / len(self.x)
        av_y = np.sum(self.y) / len(self.y)
        pow_x = self.x * self.x
        av_pow_x = np.sum(pow_x) / len(x)
        xy = self.x * self.y
        av_xy = np.sum(xy) / len(xy)
        #Print results of the sample
        #print(x,y,xy,av_x,av_y,av_pow_x,av_xy)
        #Calculate m
        self.m = (av_xy - av_x * av_y) / (av_pow_x - av_x ** 2)
        # Calculate q
        self.q = self.y[0] - self.m * self.x[0]

        return (self.m, self.q)

    def function_plot(self):
        px = np.array(range(1000))
        for n in px:
            py = self.m * px + self.q
        #Show [x, y] points
        plt.plot(self.x, self.y, 'ro')
        #Show the predicted function
        plt.plot(px, py)
        plt.show()

