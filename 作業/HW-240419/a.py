x='I saw a saw saw salsa while sawing salsa with my salsa sawing saw.'

x=x.replace('.',' ')#去掉句號方法1(推薦)
#去掉句號方法2 (x=x[:len(x)-1])

x=(x.lower()).split()#轉小寫後,以空白為依據分割成串列
#['i','saw','a','saw','saw','salsa','while','sawing','salsa','with','my','salsa','sawing','saw']

for z in set(x):
    print(f'{z}出現{x.count(z)}次')