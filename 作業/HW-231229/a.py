v=[]
for a in range(10):
    a=int(input('請輸入整數(共10次):'))
    v.append(a)
print(f'最大值:{max(v)}\n最小值:{min(v)}\n總和:{sum(v)}\n平均:{sum(v)/10}')