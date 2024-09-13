z=set()
while len(z)!=20:
    x=int(input('輸入整數:'))
    if x in z:
        print('請勿重複!')
    z.add(x)
print(sorted(z,reverse=True))
'''
z=[]
while len(z)<20:
    x=int(input('輸入整數:'))
    if x in z:
        print('請勿重複!')
    else:
        z.append(x)
z.sort(reverse=True)
print(z)
'''
#----------------------------------
'''
z=list()
while True:
    x=int(input('輸入整數:'))
    if x in z:
        print('請勿重複!')
    z.append(x)
    if z.count(x)>1:
        z.remove(x)
    if len(z)==20:
        break
print(sorted(z)[::-1])
'''