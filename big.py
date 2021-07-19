# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:21:36 2021

@author: ADMIN
"""
from time import time
a,b,c = eval(input('enter three numbers'))
t1=time()
'''1st method '''
if(a>b and a>c):
    print('big ',a)
if(b>a and b>c):
    print('big ',b)
if(c>a and c>b):
    print('big ',c)
t2=time()
print('total time required ',t2-t1)  

'''2nd '''

big = a
if(big<b):
    big = b
if(big<c):
    big = c
    
print('big in 2nd method:  ',big)


'''3rd '''

if(a>b):
    if(a>c):
        big = a
    else:
        big = c
else:
    if(b>c):
        big = b
    else:
        big = c
print('big in 3rd method:  ',big)
