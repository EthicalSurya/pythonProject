from multipledispatch import dispatch

@dispatch(int,int,int)
def add(a,b,c):
    print(a+b+c)

@dispatch(int,int)
def add(a,b):
    print(a+b)

add(2,7)
