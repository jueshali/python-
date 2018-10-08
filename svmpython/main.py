# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:22:58 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

c = 10
kerneltype = "liner"

n = 50

X1 = scio.loadmat("matlabx1")
X2 = scio.loadmat("matlabx2")
Y1 = scio.loadmat("matlaby1")
Y2 = scio.loadmat("matlaby2")

x1 = X1["x1"]
x2 = X2["x2"]
y1 = Y1["y1"]
y2 = Y2["y2"]

plt.figure(1)
plt.scatter(x1[0],x1[1],c="g")
plt.scatter(x2[0],x2[1],c="r")


X = np.hstack((x1,x2))
Y = np.hstack((y1,y2))