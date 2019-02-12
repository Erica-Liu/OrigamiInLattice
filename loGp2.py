#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:18:06 2019

@author: yuqingliu
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta_1 = np.pi/3
theta_2 = np.pi/3

X_1 = np.arange(-3,3,0.1)
Y_1 = np.arange(-3,3,0.1)
X_1, Y_1 = np.meshgrid(X_1, Y_1)
Z_1 = 0


surf_1 =  ax.plot_surface(X_1, Y_1, Z_1, color = 'b')



Y_2 = np.arange(-3, 3, 0.25)
X_2 = np.arange(3 - 6* math.cos(theta_2),3,0.1)
Y_2, X_2 = np.meshgrid(Y_2, X_2)
Z_2 = (3 - X_2)*math.tan(theta_2)


surf_2 =  ax.plot_surface(X_2, Y_2, Z_2, color = 'r')

Y_3 = np.arange(-3,3, 0.25)
X_3 = np.arange(-3, -3 + 6*math.cos(theta_1),0.1)
X_3, Y_3 = np.meshgrid(X_3, Y_3)
Z_3 = (3 + X_3)*math.tan(theta_1)
surf_3 = ax.plot_surface(X_3, Y_3, Z_3, color = 'g')

plt.show()


