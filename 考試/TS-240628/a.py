et=input('請輸入寬與高，以逗號隔開:')
a,b=tuple(map(int,et.split(',')))
for z in range(b):
    print('*'*a)