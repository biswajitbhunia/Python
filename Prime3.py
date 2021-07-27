n=eval(input('enter a number'))
m=int(n/2)
for i in range(2,m):
     r=n%i
     if r==0:
          break
if r!=0:
     print('prime')
else:
     print('not prime')

