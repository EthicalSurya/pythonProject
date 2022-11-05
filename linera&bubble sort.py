pos=-1
def search(list,n):
    i=0
    while i<(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False


list=[9,7,8,4,5]
n=5
if search(list,n):
    print("found at:",pos)
else:
    print("Not found")
print("len of list is:",len(list))

#---Bubble sort--------------------


def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

l=[5,3,8,6,7,2]
sort(l)
print(l)
