# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:58:05 2019

@author: rony
"""

#graphs
import numpy as np
import matplotlib.pyplot as plt
#%%%
x = np.linspace(0,10,100)
x
np.sin(x)
fig = plt.figure()
plt.plot(x, np.sin(x))
plt.show()
#%%%
x = np.arange(0,10)
y = x^2
x
y
#labling the axis
plt.title("graph Drawing")
plt.xlabel("time")
plt.ylabel("distance")
plt.plot(x,y)
#%%%
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(1.5,-1.5)
#%%%
#axis together
plt.plot(x, np.sin(x))

plt.axis('tight')
plt.axis([-1,11,-2,2])
#%%%
#multiple curves
plt.plot(x,np.cos(x), label=' X Curve')
plt.plot(x, np.tan(x), label='y Curve')
plt.title('sin and cos curve')
plt.ylabel("roy")
plt.xlablel("boy")
plt.axis('equal')
plt.legend()
#%%%
x = np.linspace(0,10,1000)
ax= plt.axes()
ax.plot(x,np.sin(x))
ax.set(xlim=(0,10) , ylim = (-2,2), xlabel = 'X Label' , ylabel= 'y label', title='plot with sin and cos curve');
#%%%
#box plot
import pandas as pd
plt.boxplot(df.A)
