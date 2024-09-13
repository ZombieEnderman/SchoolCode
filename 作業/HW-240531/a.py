def isPrime(x):
    if x==1:#1非質數
        return False

    a=[1,x]#因數存放處
    for z in range(2,x):#範圍2~自身
        if x%z==0:#是因數
            a.append(z)#因數已超過2個
            break#沒有繼續的必要

    if len(a)==2:#除了自身與1之外，無其他因數
        return True#是質數
    return False#非質數(因數超過2個)

x=int(input('請輸入正整數:'))
if isPrime(x):
    print('輸入值為質數')
else:
    print('輸入值不是質數')