# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:43:15 2021

@author: ADMIN
"""
from time import time
import math
n = eval(input('enter any number'))
t1=time()
for i in range(2,n-1):
    r = n%i
    if(r==0):
        break
if(r==0):
    print('Not prime')
else:
    print('prime')
t2=time()
print(t2-t1)


t1=time()
for i in range(2,int(n/2)):
    r = n%i
    if(r==0):
        break
if(r==0):
    print('Not prime')
else:
    print('prime')
t2=time()
print(t2-t1)


t1=time()
for i in range(2,int(math.sqrt(n))):
    r = n%i
    if(r==0):
        break
if(r==0):
    print('Not prime')
else:
    print('prime')
t2=time()
print(t2-t1)
