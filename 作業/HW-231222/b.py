x=[]
r=int(input('請輸入整數:'))
while r!=0:
    if r%2==0:
        x.append(r)
    else:
        x.insert(0,r)
    r=int(input('請輸入整數:'))
print(x)