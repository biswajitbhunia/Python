# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:43:06 2021
Algorithm suggested by Prof. Shibaj Banerjee, St. Xavier College
@author: Prof. Arunava Adhikari
"""
div=1
def strikeout(x):
    return x==div or x%div!=0

from time import time
n=eval(input("enter a number within which all prime numbers will be displayed"))
t1=time()
a=list(range(2,n+1))
'''print(a)'''
for i in a:
    div=i
    a=list(filter(strikeout,a))
t2=time()
print(a)
print('total ',len(a),'prime numbers')
print(t2-t1)
