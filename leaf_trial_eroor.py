# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:38:42 2020

@author: koust
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 04:30:50 2020
@author: koustav
"""

import matplotlib.pyplot as plt 
import random as rand

x = []  # List to store x values
y = []
v = []  # how many numbers are being generated 
 
x.append(0)  # Let start with 0,0 
y.append(0) 

c = 0  # main counter 
c1 = 0 # Individual case visit counter
c2 = 0
c3 = 0
c4 = 0  
for i in range(5000): 
    z = rand.random()
    v.append(z)
    if z>=.01 and z<.60:
        x1=(19.05 * (x[c]) + 0.72 * (y[c]) + 1.86) / (5.36 * (x[c]) + 2.01 * (y[c]) + 20)
        y1=(-0.15 * (x[c]) + 16.9 * (y[c]) - 0.28) / (5.36 * (x[c]) + 2.01 * (y[c]) + 20)
        x.append(x1)
        y.append(y1)
#        c1 += 1
#        c = c+1
     
    if z>= .60 and z<=.61 :
        x2=(0.20 * (x[c]) + 4.4 * (y[c]) + 7.5) / (0.2 * (x[c]) + 8.8 * (y[c]) + 15.4)
        y2=(-0.3 * (x[c]) - 4.4 * (y[c]) - 10.4) / (0.2 * (x[c]) + 8.8 * (y[c]) + 15.4)
        x.append(x2)
        y.append(y2)
#        c2 += 1
#       c = c+1
        
    if z>.61 and z<=.81: 
        x3=(96.5 * (x[c]) + 35.2 * (y[c]) + 5.8) / (134.8 * (x[c]) + 30.7 * (y[c]) + 7.5)
        y3=(-131.4 * (x[c]) - 6.5 * (y[c]) + 19.1) / (134.8 * (x[c]) + 30.7 * (y[c]) + 7.5)
        x.append(x3)
        y.append(y3)
        c3 += 1
#       c = c+1
        
    if z>.81 and z<=1.00: 
        x4=(-32.5 * (x[c]) + 5.81 * (y[c]) - 2.9) / (-128.1 * (x[c]) - 24.3 * (y[c]) - 5.8)
        y4=(122.9 * (x[c]) - 0.1 * (y[c]) - 19.9) / (-128.1 * (x[c]) - 24.3 * (y[c]) - 5.8)
        x.append(x4)
        y.append(y4)
#        c4 += 1
    c = c+1
    print(c,'\n')
plt.scatter(x, y, edgecolor ='green') 
#plt.scatter(x, y,s = 0.2, edgecolor ='green')        
plt.show() 