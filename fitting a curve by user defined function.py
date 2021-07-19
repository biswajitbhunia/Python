#!/usr/bin/env python
# coding: utf-8

# In[12]:


from math import *
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.arange(0,6,0.2)
y = np.array([0,0.151,0.349,0.572,0.759,0.941,1.029,1.057,1.091,1.125,1.197,1.177,1.102,1.082,0.974,0.967,0.848,0.819,0.773,0.699,0.647,0.582,0.540,0.488,0.436,0.393,0.372,0.332,0.306,0.282])

def f(x,a,b):    return a*exp(-b*x**2)     #user defined fitting function

para, var  = curve_fit(f,x,y)

print('parameters are:', para)

plt.figure(figsize = (12,9))
plt.plot(x1, y1, 'k.')
plt.plot(x1, f(x1, para[0], para[1]), 'r-', label = 'fitted curve')
plt.legend(loc = 'best')
plt.show()


# In[ ]:





# In[ ]:




