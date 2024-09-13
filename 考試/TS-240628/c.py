from spw import isPrime,divisor
et=int(input('請輸入2~100的整數:'))
prdiv=[]#質因數

def sb(x):
    n=1
    for z in x:
        n*=z
    return n


if et not in range(2,101):
    print('無法處理')

else:
    div=divisor(et)#初始因數
    div2=[]#合因數
    for z in div:
        if isPrime(z):#是質數就加入質因數
            prdiv.append(z)
        else:#不是質數就加入合因數
            div2.append(z)

    for z in div2:#獲取合因數
        a=tuple(filter(isPrime,divisor(z)))#留下質數
        for y in a:#質數丟質因數
            prdiv.append(y)

    while sb(prdiv)!=et:
        if sb(prdiv)>et:
            prdiv=list(set(prdiv))
        elif sb(prdiv)<et:
            for z in prdiv:
                if sb(prdiv)*z==et:
                    prdiv.append(z)

prdiv=sorted(map(str,prdiv))
print('*'.join(prdiv))