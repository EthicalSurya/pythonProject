#
# # def add(a=None,b=None,c=None):
# #     if a!=None and b!=None and c!=None:
# #         print(a+b+c)
# #     elif a!=None and b!=None:
# #         print(a+b)
# #     else:
# #         print(a)
# #
# # add(5,4)
# #
# #
# # def is_leap(year):
# #     leap=False
# #     if year%400==0:
# #         leap=True
# #     elif year%100==0:
# #         leap=False
# #     elif year%4==0:
# #         leap=True
# #     return leap
# #
# #
# # year=int(input("Enter any year"))
# # print(is_leap(year))
# #
# # def div(a,b):
# #     if a<b:
# #         a,b=b,a
# #     return a/b
#
# # x=div(2,4)
# # print(x)


# n=1
# while n<=10:
#     return n**2
#     n+=1

def is_prime(n):
    if n==0 or n==1:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

res=is_prime(6)
print(res)


# def Fibonacci(n):
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    # elif n == 0:
    #     return 0

    # Check if n is 1,2
    # it will return 1
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# # Driver Program
# print(Fibonacci(9))

l1=[2,5,6,7,8,9,1]
res=list(filter((lambda x:x%2==0),l1))

print(res)

ls=["Anil", "Surya", "Ravi", "Anand", "sridhar"]
def select_name(ls,char):
    new_lis=[]
    for i in ls:
        if i.startswith(char):
            new_lis.append(i)
        return new_lis
print(select_name(ls,'A'))


l2=[2,4,5,6,8]

# def sqr(l2):
#     new_lis=[]
#     for i in l2:
#         new_lis.append(i*i)
#     return new_lis
# print(sqr(l2))

res=list(map(lambda x:x*x,l2))
print(res)

from functools import reduce
l2=[2,4,5,6,8]
res=reduce((lambda x,y:x+y),l2)
print(res)

l3=[19,1,27,12,87,10,61,2]

# def larger(l3):
#     large=0
#     for i in l3:
#         if i>large:
#             large=i
#     return large
#  print(larger(l3))
res=reduce((lambda x,y:x if x>y else y),l3)
print(res)

fruits=['apple','mango','cherry', 'kiwi']
# new_lis=[]
#
# for i in fruits:
#     if "a" in i:
#         new_lis.append(i)
# print(new_lis)

new_lis=[x for x in fruits if "a" in x]
print(new_lis)


class A:
    def __init__(self,a,b):
        print("This is class A constructor")
        self.a=a
        self.b=b
        print(self.a+self.b)
class B:
    def __init__(self,a,b):
        print("This is class B constructor")
        self.a=a
        self.b=b
        print(self.a+self.b)

a=A(4,5)
b=B(5,5)


class M:
    def __init__(self):
        print("This is class M constructor")
class N(M):
    def __init__(self):
        print("This is class N constructor")
        # super().__init__()
        M.__init__(self)  #same as super()

n=N()

n=[2,4,6,8]

for i in n:
    sq= i*i
    print(sq,end=",")

print()

cars={
    "Brand":"Ford",
    "Model":"SUV",
    "year"  : 2009
}

print(cars["Brand"])
print(cars.get("Brand"))

print("Before Modification")
print(cars.items())
print("After Modification")
cars["color"]="Red"
print(cars.items())


pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
   pass
   if (p == 0):
       current = p
       break
   elif (p % 2 == 0):
       continue
   print(p,end=" ")    # output => 1 3 1 3 1
print("\n",current)    # output => 0

import array as arr

a=arr.array("i",[2,3,4,5])

print(a[1])

# -----Guess the number-------------------
actual_num=45
attempts=0

while True:

    guess=int(input("Guess the no"))
    attempts += 1
    if guess > actual_num:
        print("Your gues was too high")
    elif guess < actual_num:
        print("Your gues was too low")
    else:
        print(f"you guessed the num in {attempts} attempt(s)")
        break

    if attempts>9:
        print("game over")
        break
print("Thanks for playing")

n= int(input("Enter a dig to check for prime"))

for i in range(2,n):
    if n%i is 0:
        print(f"{n} is not a prime")
        break
else:
    print("{} is prime".format(n))


def display(Num):
    if Num % 3 == 0 and Num % 5 == 0:
        print("Zoom")

    elif Num % 3 == 0:
        print("Zip")

    elif Num % 5 == 0:
        print("Zap")

    else:
        print("Invalid")


# Main code
if __name__ == "__main__":
    Num = 9

    # Function call
    display(Num)

    Num = 10
    display(Num)

    Num = 15
    display(Num)

    Num = 19
    display(Num)


