def fib(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a, b = b, c
            print(c)
fib(4)


lst=[24,15,16,17,19,21,38]

evn=[]
odd=[]

for i in lst:
    if i%2 is 0:
        evn.append(i)
    else:
        odd.append(i)
print(evn)
print(odd)







