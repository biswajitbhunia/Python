n=input('enter a number')
m=math.sqrt(n)
for i in range(2,m):
     r=n%i
if r==0:
break
if r!=0:
print('prime')
else
print('not prime')

