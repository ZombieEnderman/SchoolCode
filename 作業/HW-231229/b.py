x=[23,21,22,2,13,23,12,31,32]
m=int(input('輸入最大值m:'))
n=int(input('輸入最小值n:'))
y,z,w=0,0,[]
for b in x:
    if m<b:
        w.append(b)
    if n>b:
        z+=1
    if m>b>n:
        y+=1
print(f'大於m的數:{w}\n小於n的數有{z}個\n介於m與n之間的數有{y}個')