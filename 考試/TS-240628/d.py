def add_left(x,y):
    """
#no return
add_left([10],20)->[20,10]"""

    x.insert(0,y)

def add_right(x,y):
    """
#no return
add_right([10],30)->[10,30]"""

    x.append(y)

def pop_left(x):
    """
pop_left([10,30])->10
pop_left([])->None"""

    if len(x)!=0:
        return x.pop(0)
    return

def pop_right(x):
    """
pop_right([10,30])->30
pop_right([])->None"""

    if len(x)!=0:
        return x.pop(-1)
    return

#------------------------------------
x=[10]
add_left(x,20)
print(x)#[20,10]
add_right(x,30)
print(x)#[20,10,30]
a=pop_left(x)
print(a,x)#[10,30]
a=pop_right(x)
print(a,x)#[10]

a=pop_left(x)
print(a,x)#[]
a=pop_right(x)
print(a,x)#[]