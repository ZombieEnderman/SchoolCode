c=[]
while True:
    b=input('請輸入單字:').lower()
    if b=='quit':
        break
    else:
        b=list(b)
        for z in b:
            c.append(z)
a={z:c.count(z) for z in 'aeiou'}
for z in a:
    print(f'{z} {a[z]}次')