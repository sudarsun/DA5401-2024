#!/usr/bin/python3
# motivated by https://www.youtube.com/shorts/I8yqEjUM9Zw
# an attempt is made to generate Mandelbrot Quintet

import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import queue

# a simple function to generate 5 points from one input point
def gen_points(p:np.array, A:np.array):
    Ax = np.matmul(p, A)
    p1 = Ax + np.array([0,1])
    p2 = Ax + np.array([-1,0])
    p3 = Ax + np.array([1,0])
    p4 = Ax + np.array([0,-1])
    return Ax, p1, p2, p3, p4

# let's define the colors for those 5 different points
colors = ['yellow','red','blue','brown','green']
# define the transformation matrix
A = np.array([[0.2, 0.4],[-.4, 0.2]])
# consider an arbitrary starting point
x = np.array([.15, .2])

# create placeholders to collect the data.
data = []
label = []

# setup the queue to process over all the generated points.
q = queue.Queue()
# put the first point into the queue.
q.put(x)

# let's process the queue items limited by the loop limit.
for i in range(3000):
    # pop the data from the queue
    x = q.get()
    # generate the next 5 points for the popped point.
    ax, p1, p2, p3, p4 = gen_points(x, A)
    # collect the labels
    label.extend([0,1,2,3,4])
    # collect the generated points.
    data.extend([ax, p1, p2, p3, p4])
    # queue the points for further processing.
    q.put(ax)
    q.put(p1)
    q.put(p2)
    q.put(p3)
    q.put(p4)

    # every 100 iterations, let's plot the data to view the animation.
    if i > 0 and i%100==0:
        pdata = np.array(data)
        plt.scatter(pdata[:,0], pdata[:,1], 1, c=label, cmap=clr.ListedColormap(colors))
        plt.draw()
        plt.pause(.1)
        plt.clf()
        