# using 'with' block we need not close the file explicitly

with open("Harry Bhai ka code") as f:
    a=f.readlines()
    print(a)


# without using 'with'
f=open("Harry Bhai ka code","rt")
print(f.read())
f.close()

l=10

def fun():
    m=8
    #global l
    l=15

    print(m,l,"hi helloo")
fun()
print(l)

print("\\narry is a gud boy")

