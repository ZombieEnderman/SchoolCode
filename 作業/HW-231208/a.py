a=b=None
x=int(input('輸入正整數,輸入0可離開:'))
if x!=0:
    a=b=x
    while x!=0:
        if x<a:
            a=x
        if x>b:
            b=x
        x=int(input('輸入正整數,輸入0可離開:'))
if (a==None)or(b==a):
    print('沒有最大、最小值!')
else:
    print(f'最小值:{a}\n最大值:{b}')