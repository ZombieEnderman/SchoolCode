why1=list(map(int,input(f'請輸入第1組數值,以逗號隔開:').split(',')))
why2=list(map(int,input(f'請輸入第2組數值,以逗號隔開:').split(',')))
why3,n=[],0
for z in range(min(len(why1),len(why2))):
    why3.append(why1[z])
    why3.append(why2[z])
    n+=1
why3.extend(why1[n:])
why3.extend(why2[n:])
print(why3)