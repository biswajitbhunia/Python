from turtle import *
reset()
for i in 'abcd':
	forward(100)
	right(90)

'''Second Part of Turtle'''
reset()
c = 'red'
for i in 'abcd':
    color(c)
    if c=='red':
        c='green'
    elif c=='green':
        c='blue'
    else:
        c='red'
    forward(100)
    right(90)
