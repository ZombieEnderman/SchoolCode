ro='C:\\Users\\iStudent\\Desktop\\yee\\data.txt'
f=open(ro)
for z in f:
    z=z.strip()
    if z.startswith('j'):
        print(z)

f.close()