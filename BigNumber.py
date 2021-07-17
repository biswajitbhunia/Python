'''Biggest number using three different method '''

l = [2, 5, 3, 4, 8, 10, 3]

''' using loop '''
m = l[0]
for i in l:
    if m < i:
        m = i
print(f'Biggest number: {m}')

''' using loop  using index'''
m1 = l[0]
for i in l[1:]:
    if m1 < i:
        m1 = i
print(f'Biggest number: {m1}')

'''another process : us min() function '''
m = max(l)
print(f'Biggest number: {m}')

'''another process : us sort() function '''
l.sort()
m = l[6]
print(f'Biggest number: {m}')
