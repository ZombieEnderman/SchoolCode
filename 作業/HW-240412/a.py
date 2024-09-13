a=[]
while len(a)<30:
    x=input('輸入個位數30個:')
    if len(x)==1:
        a.append(int(x))
    else:
        print('請輸入個位數!')
b={z:a.count(z) for z in a}
for z,y in b.items():
    print(f'{z}出現{y}次')
'''
a=[]#原資料
while len(a)!=30:
    x=int(input('輸入個位數30個:'))
    if x/10<1:#判斷個位數
        a.append(x)
    else:
        print('請輸入個位數!')
b=set(a)
for z in b:
    print(f'{z}出現{a.count(z)}次')
'''