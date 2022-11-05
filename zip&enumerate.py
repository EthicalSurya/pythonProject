l1=["Maths","English","Social","Science"]
l2=[85,92,75,67]
x=zip(l1,l2)
print(x)
y=list(x) #tuples,dict can also be used but the returned iterables are in tuple form
print(y)
z=list(zip(*y)) #unzip
print(z)

# Enumerate

l=["cars","bikes","phones","tabs"]

for index,items in enumerate(l):
    if index%2 is 0:
        print(f"please buy {items}")





