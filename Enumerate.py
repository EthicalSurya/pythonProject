ls=['bhendi','aloo','chopstick','chowmein']
# i=1
# for item in ls:
#     if i%2!=0:
#         print(item)
#     i+=1

for index,item in enumerate(ls):
    if index%2==0:
        print(f"jarvis please buy {item}")

class A:
    def __init__(self):
        print("This is class A const")

    def add(self,a,b):
        return a+b
class B:
    def __init__(self):
        print("This is class B const")
        super().__init__()
    def mul(self,a,b):
        return a*b

class C(B,A):
    def __init__(self):
        print("This is class C const")
        super().__init__()
    def div(self,a,b):
        return a//b

c=C()
print(c.add(3,5))
print(c.mul(3,5))
print(c.div(10,5))

l1=[2,3,4,6,8]

def task(l1,n):
    res=l1[n:]+l1[:n]
    return res
    # sqr=[x**2 for x in res]
    # return sqr
print(task(l1,2))