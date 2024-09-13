a=[0,1]
for i in range(30):
    a.append(a[-1]+a[-2])#a=[0,1,1](1)-->a=[0,1,1,2](2)
    print(a[i])