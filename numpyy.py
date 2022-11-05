import numpy as np

arr = np.array(([1, 2, 3, 4, 5]),np.int64) #Dynamically creating 64bit memory
print(arr)
print(arr.dtype) # returns the data type of the array

import numpy as np
arr=np.array([1.2,3.2,4.2])
new_arr=arr.astype("i") #datatype conversion float to int
print(new_arr)
print(new_arr.dtype)

grt_num= lambda x,y: x if x>y else y
print(grt_num(2,3))

li=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x:x%2==0,li))
print(res)

import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2)) #Joining two arrays
print(arr)

"""import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)"""

'''import numpy as np
arr1=np.arange(1,7).reshape(3,2)
print(arr1)
arr2=np.arange(8,14).reshape(3,2)
print(arr2)

arr=np.concatenate((arr1,arr2))
print(arr)'''

import numpy as np
arr1=np.arange(1,7).reshape(3,2)
print(arr1)
arr2=np.arange(8,14).reshape(3,2)
print(arr2)
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

import numpy as np
a=np.array([11,12,13,14])
print(a)
#x=np.array_split(a,3) #split() for equal div
#print(x)
x=np.array_split(a,3)
print(x)

from numpy import *

m1= matrix('2 4 5 6 ; 5 6 7 8 ; 7 8 9 1' )
print(m1)
print(diagonal(m1))

thisset = {"apple", "banana", "cherry"}

myset={x for x in thisset if 'banana' in x}
print(myset)
print(type(myset))

from numpy import *
c1=array([2,4,5,3,9])
c2=c1.view()
c1[0]=6
print(c1)
print(c2)

def myinfo(name,**other):
    print(f"my name is {name}")
    print(other)

myinfo('Surya',age=24,mob=7075190036)


a,b=4,2



