#Function Definition using def keyword
def f():
    print('This is function')

#Calling a function
f()

#Use of Single Arguments
def f(firstName):
      print(firstName + " Bhunia")

f("Biswajit")
f("Kakali")
f("Srijita")
f('Ayush')
#.................................................
'''use of Arguments'''

def f(firstName,lastName):
      print(firstName + ' ' + lastName)

f("Biswajit", "Bhunia")

'''use of multiple arguments with * '''

def f(*nm):
      print('Second Name is : '+nm[1])

f("Biswajit", "Srijita","Ayush")

''' Using Keywords/kwargs arguments in Python'''

def f(arg1, arg2, arg3, arg4):
    print('Second Name is : '+arg2)
f(arg1='Biswajit',arg2='Srijita',arg3='Ayush',arg4='Kakali')

'''Arbitary Keywords/**kwargs arguments in Python'''

def f(**nm):
      print('Second Name is : '+nm['second'])

f(first="Biswajit", second="Srijita",third="Ayush")

'''Default Parameter Value'''
def f(nm='Srijita'):
    print('Your name : '+nm)
f('Biswajit')
f()


'''List of Arguments'''

def f(nm):
      for i in nm:
          print(i)

m = ["Biswajit", "Kakali", "Srijita","Ayush"]
f(m)

'''Returning Value'''

def sq(n):
    return n*n;
print(sq(9))

'''Empty function raises an error/exception, we can use pass statement'''
def n():
    pass

'''Recursive Function'''
'''Factorial of n'''
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(5))


'''Using Local and Global Variable'''

fn='Biswajit' #Global Variable
def f():
    global fn2 #Global Variable within f()
    fn2='Srijita'
    print('My Name : '+fn)
    print('My Mother : '+fn2)
f()
print('My Mother : '+fn2) #Since it is Global define in f() using global keyword
print('My Name : '+fn) #It is Global by default
#Can modify global varible
fn='Dipankar'
fn2='Dipika'
print('My Mother : '+fn2)  #before executing f()
f()
print('My Mother : '+fn2) #after executing f()

#Use of outer and inner function

def outer():
    a=10
    b=30
    def inner():
        a=20
        c=25
        print('Beside the inner(), a: ',a) #it is declared also in outer()
        print('Declared at outer(), b: ',b)
        print('Declared at inner(), c: ',c)       
    #calling inner function from outer function
    print('Beside the outer() , a: ',a)
    inner()
#calling Outer function
outer()


#lambda function: single line function without name, it can not access global variables.

s=lambda a,b:a+b
print('Sum= ',s(10,20))





    
