#Def Fibonacci Function
def fib(x):

# First two terms & defaults set
    n1, n2 = 1, 1
    count = 0

# Main body of the function
    if (x<0):
        print("Please enter a valid integer")
    elif(x==1):
        print("Series contains only one term")
        print(n1)
    else:
        while count<x:
            nth = n1+n2
            #Now update values
            fibSeq.append(n1)
            n1=n2
            n2=nth
            count += 1
        
# Lets take the input to know about number of terms
fibSeq = []
term = input("How many terms are there in the Fabonacci sequence?\nAns: ")
fib(term)

# So we stored the items now we should draw the squares and spiral
import turtle
turtle.reset() #This will bring the canvas
def draw_square(side_length):  #Function for drawing a square
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)

nr_squares=len(fibSeq)
# I want to fill some random color in the boxes
import random
color = ['#ebae34','#34ebd5','#7bc5ed','#f0b9d3','#ed9f80']

# Lets draw the squares
factor = 3                        #Enlargement factor
turtle.penup()
turtle.goto(50,50)                  #Move starting point right and up
turtle.pendown()
for i in range(nr_squares):
    col = random.choice(color)      #Choose a random color & fill it
    turtle.fillcolor(col)
    turtle.begin_fill()
    draw_square(factor*fibSeq[i])       #Draw square
    turtle.end_fill()
    turtle.penup()                        #Move to new corner as starting point
    turtle.forward(factor*fibSeq[i])
    turtle.right(90)
    turtle.forward(factor*fibSeq[i])
    turtle.pendown()
    

turtle.penup()
turtle.goto(50,50)       #Move to starting point
turtle.setheading(0)   #Face the turtle to the right
turtle.pencolor('black')
turtle.pensize(3)
turtle.pendown()
#Draw quartercircles with fibonacci numbers as radius
for i in range(nr_squares):
    turtle.circle(-factor*fibSeq[i],90)  # minus sign to draw clockwise


