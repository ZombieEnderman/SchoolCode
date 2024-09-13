a=[]
for _ in range(20):
    x=int(input('輸入整數:'))
    if x not in a:
        a.append(x)
print(a)
'''
a=set()
for _ in range(20):
    x=int(input('輸入整數:'))
    a.add(x)
print(list(a))
'''
#--------------------------------------------
'''
print(list(set(map(int,input('請輸入20個整數,以空白隔開:').split()) ) ) )
'''