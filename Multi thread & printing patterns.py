'''from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=A()
t2=B()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("The End")
#------------------------------Printing Patterns-------------------
for i in range(4):
    for j in range(4-i):   #try range(i) first
        print("#",end='')
    print()'''

n=int(input("Enter any num"))

for i in range(2,n):
    if n%i==0:
        print("Not prime")
        break
else:
    print("prime")