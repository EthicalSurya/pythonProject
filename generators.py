def topten():
    n=1
    while n<=10:
        sq=n**2
        yield sq
        n+=1

val=topten()                       #print(list(topten()))
for i in val:
    print(i)

