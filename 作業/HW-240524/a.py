def divisor(x):
    w=[1,x]#因數
    for y in range(2,x):
        if x%y==0:
            w.append(y)
    return sorted(w)

x=int(input('輸入正整數:'))
print(f'{x}的因數有:')
for a in divisor(x):
    print(f'\t{a}'.expandtabs(2))