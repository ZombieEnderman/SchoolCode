def add(x,y):
    js=[]#js待回傳之串列
    if len(x)>len(y):
        x,y=y,x#控制x為最短的串列

    while len(x)!=len(y):#使長度一致
        x.append(0)

    for z in range(len(x)):#元素相加
        js.append(x[z]+y[z])
    return js

p=[1,3,5,6,8]
q=[2,3,4,5,6]
r=add(p,q)
print(r)
print(add([10,20,30],[1,2]))