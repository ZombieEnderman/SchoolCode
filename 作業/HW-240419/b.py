x='I saw a saw saw salsa while sawing salsa with my salsa sawing saw.'
x=x.lower() #轉小寫
y=list(set(x))
y.remove('.')
y.remove(' ')
#-------------------list y=['g','w','e','s','m','a','n','t','y','h','l','i']
q=[x.count(z) for z in y] #[ 2,  8,  1, 12,  1, 13,  2,  1,  1,  2,  4,  5,]
print(f'{y[q.index(max(q))]}出現最多次')