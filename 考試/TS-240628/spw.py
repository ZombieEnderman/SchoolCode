#正式碼
def avg(*x):
    """計算平均值，
可以給一堆數字，
亦可給予字串以外的可迭代物件。
{平均值將四捨五入到小數第1位}{參數不可空白!}
avg(1,2,3)->2.0;
avg([1,2,3])->2.0;
avg(range(1,4))->2.0;
avg('1','2')->錯誤!;
avg()->錯誤!"""

    if type(x[0])==list or type(x[0])==tuple or type(x[0])==set:#導入資料為串列、元組、集合
        x=x[0]#解包元組
        return round(sum(x)/len(x),1)#回傳平均值

    elif type(x[0])==range:#導入資料為range物件
        x=x[0]#解包元組
        x=tuple(x)#將range物件轉成元組
        return round(sum(x)/len(x),1)#回傳平均值

    elif type(x[0])==dict:#導入資料為字典
        x=x[0]#解包元組
        tota=0#總和
        for z in x:#取得鍵
            if type(z)==int or type(z)==float:#判斷鍵是否為數值
                bl=True
            else:
                bl=False
            break
        if bl:#鍵是數值
            for z in x:
                tota+=z#加總鍵
        else:#鍵不是數值
            for z in x:
                tota+=x[z]#加總值
        return round(tota/len(x),1)#回傳字典平均值

    return round(sum(x)/len(x),1)#導入資料是多個數值


def max_num(x,n=1):
    """回傳可迭代物件中第n+1大的元素。
#格式:(可迭代物件,整數)
{可迭代物件必填，且不能是字串}{整數不填預設為1}
max_num([9,1,3,7])->7;
max_num([9,1,3,7],2)->3;
max_num(range(11))->9;
max_num(['1','2','3'])->錯誤!;
max_num()->錯誤!"""

    if type(x)==list:#導入資料為串列
        x_copy=x[:]#複製一份
        for _ in range(n):
            x_copy.remove(max(x_copy))
        return max(x_copy)

    elif type(x)==tuple or type(x)==set or type(x)==range:#導入資料為元組、集合、range物件
        x_copy=list(x)#轉串列
        for _ in range(n):
            x_copy.remove(max(x_copy))
        return max(x_copy)

    else:#導入資料為字典
        for z in x:
            if type(z)==int or type(z)==float:#鍵是數值
                x_copy=[z for z in x]#鍵當串列元素
            else:#值是數值
                x_copy=[z for z in x.values()]#值當串列元素

        for _ in range(n):
            x_copy.remove(max(x_copy))
        return max(x_copy)


def min_num(x,n=1):
    """回傳可迭代物件中第n+1小的元素。
#格式:(可迭代物件,整數)
{可迭代物件必填，且不能是字串}{整數不填預設為1}
min_num([6,4,2])->4
min_num([6,4,2],2)->2
min_num(range(11))->1
min_num(['2','4','6'])->錯誤!;
min_num()->錯誤!"""

    if type(x)==list:#導入資料為串列
        x_copy=x[:]#複製一份
        for _ in range(n):
            x_copy.remove(min(x_copy))
        return min(x_copy)

    elif type(x)==tuple or type(x)==set or type(x)==range:#導入資料為元組、集合、range物件
        x_copy=list(x)#轉串列
        for _ in range(n):
            x_copy.remove(min(x_copy))
        return min(x_copy)

    else:#導入資料為字典
        for z in x:
            if type(z)==int or type(z)==float:#鍵是數值
                x_copy=[z for z in x]#鍵當串列元素
            else:#值是數值
                x_copy=[z for z in x.values()]#值當串列元素

        for _ in range(n):
            x_copy.remove(min(x_copy))
        return min(x_copy)


def fatl(x=1):
    """計算階乘。
{僅能一次導入一個參數，且不能是0}{參數不填預設為1}{參數必須是整數!}
#公式:n!=n*(n-1)...*1。
fatl()->1;
fatl(3)->6;
fatl(4)->24;
fatl(2.4)->錯誤!;
fatl(0)->錯誤!;
fatl(-7)->錯誤!"""

    if x==1:#1階乘為1
        return 1
    else:
        return x*fatl(x-1)


def fs(x=0):
    """計算費氏數列。
{僅能一次導入一個參數}{參數不填預設為0}{參數必須是正整數!}
#公式:fn=f(n-1)+f(n-2)。
fs()->0;
fs(1)->1;
fs(4)->3;
fs(2.5)->錯誤!;
fs(-1)->錯誤!"""

    if x==0:#第0項為0
        return 0
    elif x==1:#第1項為1
        return 1
    else:
        return fs(x-1)+fs(x-2)


def divisor(x,reverse=False):
    """以串列型態列出所有因數(由小到大)，
reverse參數設為True時，可以改由大到小列出。
#格式:(整數,reverse)
{僅能一次導入一個參數，且不可空白!}{參數必須是正整數，且不能是0!}{reverse參數預設為False}
#因數:a能被b整除，b就是a的因數
divisor(4)->[1,2,4];
divisor(4,reverse=True)->[4,2,1];
divisor(-1)->請輸入0以外的正整數!;
divisor(0)->請輸入0以外的正整數!;
divisor(1.25)->請輸入0以外的正整數!;
divisor()->錯誤!"""

    w=[1,x]#因數存放處
    if x<=0 or type(x)==float:#防止輸入0、負數、浮點數
        return '請輸入0以外的正整數!'

    for z in range(2,x):#範圍2~自身-1
        if x%z==0:#是因數
            w.append(z)

    if reverse:#參數為真
        return sorted(w,reverse=True)#回傳因數反序串列
    return sorted(w)#回傳因數正序串列(參數為假)


def isPrime(x):
    """判斷是否為質數，並回傳布林值。
{僅能一次導入一個參數，且不能是0}{參數必須是正整數!}{參數不可空白!}
#質數:除了自己跟1之外沒有其他因數的數，而1不是質數
isPrime(1)->False;
isPrime(0)->False;
isPrime(2)->True;
isPrime(4)->False;
isPrime(1.2)->None;
isPrime(-1)->None;
isPrime()->錯誤!"""

    if type(x)!=int or x<0:#禁止輸入正整數以外的值
        return None
    elif x==1 or x==0:#1、0非質數
        return False

    for z in range(2,x):#範圍2~自身
        if x%z==0:#找到因數
            return False#非質數(因數超過2個)

    return True#是質數


def isNumber(x):
    """判斷是否為數值，並回傳布林值。
{僅能一次導入一個參數}{參數不可空白!}
isNumber('1')->False;
isNumber(-2)->True;
isNumber()->錯誤!"""

    if type(x)==int or type(x)==float:
        return True
    return False


def isIterable(x):
    """判斷是否為可迭代物件，並回傳布林值。
{僅能一次導入一個參數}{參數不可空白!}
isIterable('1')->True;
isIterable(11)->False;
isIterable([1])->True;
isIterable(range(1))->True;
isIterable()->錯誤!"""

    if type(x) in ( type([]), type(()), type({}), type(set()), type(range(1)) ):
        return True
    return False


def isEven(x):
    """判斷是否為偶數，並回傳布林值。
{僅能一次導入一個參數}{參數必須是正整數!}{參數不可空白!}
isEven(2)->True;
isEven(21)->False;
isEven(-1)->None;
isEven(2.5)->None;
isEven('5')->None;
isEven()->錯誤!"""

    if type(x)!=int or x<0:#禁止輸入正整數以外的值
        return None

    elif x%2==0:#是偶數
        return True
    return False#不是偶數


def isOdd(x):
    """判斷是否為奇數，並回傳布林值。
{僅能一次導入一個參數}{參數必須是正整數!}{參數不可空白!}
isOdd(33)->True;
isOdd(44)->False;
isOdd(-11)->None;
isOdd(1.7)->None;
isOdd('7')->None;
isOdd()->錯誤!"""

    if type(x)!=int or x<0:#禁止輸入正整數以外的值
        return None

    elif x%2==1:#是奇數
        return True
    return False#不是奇數


def divisor_max(x,y):
    """列出最大公因數。
{僅能一次導入兩個參數}{兩參數皆必須是正整數!}{參數不可空白!}
#公因數:a與c皆能被b整除，b就是a與c的公因數
divisor_max(1,2)->1;
divisor_max(6,4)->2;
divisor_max(1,0)->0;
divisor_max(1.5,3)->請輸入正整數!;
divisor_max(-12,2)->請輸入正整數!;
divisor_max()->錯誤!;
divisor_max(2)->錯誤!"""

    w=[1]#公因數存放處
    if x==0 or y==0:#其中一參數是0時，回傳0
        return 0
    elif x<0 or type(x)==float:#防止輸入負數、浮點數
        return '請輸入正整數!'

    for z in range(2,min(x,y)+1):#範圍2~較小的參數
        if x%z==0 and y%z==0:#是公因數
            w.append(z)

    return max(w)


def mult_min(x,y):
    """列出最小公倍數。
{僅能一次導入兩個參數}{兩參數皆必須是正整數!}{參數不可空白!}
mult_min(2,4)->4;
mult_min(10,12)->60;
mult_min(2,0)->0;
mult_min(-2,0)->請輸入正整數!;
mult_min(2,0.5)->請輸入正整數!;
mult_min(2)->錯誤!;
mult_min()->錯誤!"""

    w=[]#公倍數存放處
    if x==0 or y==0:#其中一參數是0時，回傳0
        return 0
    elif (x<0 or y<0) or (type(x)==float or type(y)==float):#防止輸入負數、浮點數
        return '請輸入正整數!'

    for z in range(max(x,y),x*y+1):#範圍較大的參數~兩數相乘的數
        if z%x==0 and z%y==0:
            w.append(z)
    return min(w)


def prime_range(x,y,reverse=False):
    """以串列型態列出範圍內的所有質數(由小到大)，
reverse參數設為True時，可以改由大到小列出。
#格式:(起始值,結束值(包含此值),reverse)
{僅能一次導入兩個參數,且不可空白!}{reverse參數預設為False}
#質數:除了自己跟1之外沒有其他因數的數，而1不是質數
prime_range(1,10)->[2,3,5,7];
prime_range(1,10,reverse=True)->[7,5,3,2];
prime_range(1,10.5)->請輸入0以外的正整數!;
prime_range(1,0)->請輸入0以外的正整數!;
prime_range()->錯誤!"""

    w,v=[],[]#w暫存因數、v久存質數
    if (x<=0 or y<=0) or (type(x)==float or type(y)==float):#防止輸入0、負數、浮點數
        return '請輸入0以外的正整數!'

    for q in range(x,y+1):#範圍參數1~參數2
        for z in range(1,q+1):#範圍1~自身
            if q%z==0:#是因數就丟w
                w.append(z)
        if len(w)>2:#非質數
            bl=False
        else:#是質數
            bl=True
        if bl:#是質數就丟v
            v.append(q)
        w.clear()#清空暫存因數

    if 1 in v:
        v.remove(1)#1不是質數
    if reverse:
        return v[::-1]#回傳質數反序串列
    return v#回傳質數正序串列


def addvalue(x,y):
    """回傳元素相加後的新串列。
{僅能一次導入兩個可迭代物件}{參數不可空白!}{參數必須是可迭代物件!}{參數是字串時會相連}
addvalue([1,2],[9,8])->[10,10];
addvalue({4,2,0},{'g':6, 'o':4})->[10,6,0];
addvalue((1,4,1,2),{6:'g', 3:'o', 0:'i', 5:'s'})->[7,7,1,7];
addvalue(range(6),range(1,9,2))->[1,4,7,10,4,5];
addvalue('12','1')->121;
addvalue('12',1)->錯誤!;
addvalue()->錯誤!"""

    adds=[]#新串列
    n=0#計次

    #處理x型態
    if type(x)==set or type(x)==tuple or type(x)==range:#x為串列、元組、集合、range物件
        x2=list(x)

    elif type(x)==dict:#x為字典
        for z in x:#取得鍵
            if type(z)==int or type(z)==float:#判斷鍵是否為數值
                x2=[z for z in x.keys()]#把鍵變串列元素(鍵是數值)
            else:#值是數值
                x2=[z for z in x.values()]#把值變串列元素

    else:#x是串列
        x2=x[:]#複製一份

    #處理y型態
    if type(y)==set or type(x)==tuple or type(x)==range:#y為串列、元組、集合、range物件
        y2=list(y)

    elif type(y)==dict:#y為字典
        for z in y:#取得鍵
            if type(z)==int or type(z)==float:#判斷鍵是否為數值
                y2=[z for z in y.keys()]#把鍵變串列元素(鍵是數值)
            else:#值是數值
                y2=[z for z in y.values()]#把值變串列元素

    else:#y是串列
        y2=y[:]#複製一份

    #控制x2為最短
    if len(x2)>len(y2):
        x2,y2=y2,x2

    #元素相加
    for z in range(len(x2)):#加到短的結束
        adds.append(x2[z]+y2[z])
        n+=1
    adds.extend(y2[n:])#合併剩下長的
    return adds


def max_len(x,y):
    """回傳長度較長的可迭代物件，如果長度一樣就回傳字串。
{僅能一次導入兩個可迭代物件}{參數不可空白!}{參數必須是可迭代物件!}
max_len([1,2],(1,))->[1,2];
max_len({1,2},{1:1, 2:2, 3:3})->{1:1, 2:2, 3:3};
max_len(range(8),range(0,10))->range(0,10);
max_len({2},[5])->一樣長;
max_len(2,5)->錯誤!;
max_len()->錯誤!"""

    lx=len(x)
    ly=len(y)
    if lx>ly:#x較長
        return x
    elif lx<ly:#y較長
        return y
    return '一樣長'


def min_len(x,y):
    """回傳長度較短的可迭代物件，如果長度一樣就回傳字串。
{僅能一次導入兩個可迭代物件}{參數不可空白!}{參數必須是可迭代物件!}
min_len([1,2],(2,))->(2,);
min_len((4,),{6,4})->(4,);
min_len(range(9),range(11))->range(0,9);
min_len((4,),[7])->一樣長;
min_len(4,7)->錯誤!;
min_len()->錯誤!"""

    lx=len(x)
    ly=len(y)
    if lx>ly:#y較短
        return y
    elif lx<ly:#x較短
        return x
    return '一樣長'


def sort_reverse(x):
    """以串列型態回傳由大到小排序的物件。
{僅能一次導入一個參數}{參數不可空白!}{參數必須是可迭代物件!}
sort_reverse('java')->['v','j','a','a'];
sort_reverse(range(8))->[7,6,5,4,3,2,1,0];
sort_reverse()->錯誤!;
sort_reverse(2)->錯誤!"""

    return sorted(x,reverse=True)


#測試碼
if __name__=='__main__':
    print('以下為測試內容:')
    print(f"avg1:{avg(1,2,3)}")
    print(f"avg2:{avg([1,2,3])}")
    print(f"max_num:{max_num([1,7,6])}")
    print(f"min_num:{min_num(range(11))}")
    print(f"fatl:{fatl(5)}")
    print(f"fs:{fs(3)}")
    print(f"divisor:{divisor(0)}")
    print(f"isPrime:{isPrime(3)}")
    print(f"isNumber:{isNumber('99')}")
    print(f"isIterable:{isIterable(range(1))}")
    print(f"isEven:{isEven(78)}")
    print(f"isOdd:{isOdd(17)}")
    print(f"divisor_max:{divisor_max(1,0)}")
    print(f"mult_min:{mult_min(12,5)}")
    print(f"prime_range:{prime_range(1,10)}")
    print(f"addvalue:{addvalue({1:0, 9:0},{'5':8, '4':7})}")
    print(f"max_len:{max_len([1,2,3],[3])}")
    print(f"min_len:{min_len(range(7),range(6))}")
    print(f"sort_reverse:{sort_reverse('java')}")
    print('測試內容到此結束!')