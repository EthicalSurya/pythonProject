n= int(input("Enter any num"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


num=int(input("Enter any num"))
m=1
while m<=10:
    print(f"{num} X {m} = {num*m}")
    m+=1

n=int(input("Enter any num"))
factorial=1
for i in range(1,n+1): #or for i in range(n)
    factorial = factorial*i  #or factorial=factorial*(i+1)
print(f"The factorial of {n} is {factorial}")

# Pattern without inner loops
n=4
for i in range(4):
    print("*" * (i+1))

