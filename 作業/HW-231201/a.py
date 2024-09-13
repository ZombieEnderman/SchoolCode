from random import randint
t=randint(1,100)
z=1#猜測次數
c=1
b=100
print('猜數字,猜測範圍1~100')
while True:
    a=int(input('猜數字:'))
    if a>t:
        print(f'猜測錯誤!猜測範圍{c}~{a}')
        b=a
    elif a<t:
        print(f'猜測錯誤!猜測範圍{a}~{b}')
        c=a
    else:
        break
    z+=1
print(f'恭喜答對!共猜{z}次!')
