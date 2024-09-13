why1=list(map(int,input(f'請輸入第1組數值,以逗號隔開:').split(',')))
why2=list(map(int,input(f'請輸入第2組數值,以逗號隔開:').split(',')))
while len(why1)>len(why2):
    why2.append(0)
while len(why1)<len(why2):
    why1.append(0)
why3,why4=[],zip(why1,why2)
for z in why4:
    for x in z:
        if x!=0:
            why3.append(x)
print(why3)