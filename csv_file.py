'''import pandas as pd
df=pd.read_csv("C:\Python37 annual-enterprise-csv")
print(df)'''

'''n=int(input("enter any number"))
if n%2!=0:
    print("Weird")
else:
    if 2<=n<=5:
     print("Not Weird")
    elif 6<=n<=20:
     print("Weird")
    elif n>20:
     print("Not Weird")'''

'''a = int(input())
b = int(input())
print(int(a/b))
print(float(a/b))'''

'''n = int(input())
for i in range(n):
    print(i)'''

'''n=int(input())
for i in range(n):
    print(i+1,end="")'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
output = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k == n:
                continue
            else:
                output.append([i, j, k])

print(output,end='\n')