x='61,408,2,819,101,27,684,26,560,2,26,692,159,877,47,884,625,1746,886,772'
b=list(map(int,x.split(',')))
b.sort(reverse=True)
for z in b:
    print(str(z),end=' ')