import numpy as np
l1=[[10,20,30,40,50],[60,70,80,90,100]]
x=np.asarray(l1,dtype="f",order='F')# 'F' = column Major #default will be "C" row major
print(x)

import numpy as np
s=b"welcome" #ByteString
x=np.frombuffer(s,dtype='S1',count=-1,offset=0) #by default count=-1 & offset=0
print(x)

import numpy as np
s=b"welcome"
x=np.frombuffer(s,dtype='S1',count=3,offset=3) #offset=index
print(x)

import numpy as np
t=(1,2,3,4)
#x=np.fromiter(t,dtype='f',count=-1) #by default count=-1
x=np.fromiter(t,dtype='f',count=3)
print(x)

import numpy as np
x=np.zeros((3,2)) #array with 0 as its elemts will be created in the given shape
print(x)

import numpy as np
x=np.zeros((2,3),dtype='i') #array with int dtype
print(x)

import numpy as np
x=np.ones((2,3),dtype='i') #ones() array with int dtype
print(x)

import numpy as np
x=np.full((2,3),50) #full() array with value 50
print(x)

import numpy as np
x=np.eye((3),dtype='i') #eye() array with 1's on diagonal pos &0's at non-diagnonal pos
print(x)

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr) #before ravel 2-D array
print(arr.shape) #2,4 matrix
a=arr.ravel()#after ravel 1-D array
print(a.shape)

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
x=arr.T #transpose rows into cols and viceversa
print(x)

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
x=arr.flat #iterable obj
for i in x:
    print(i)
print(end='\n')
print(arr.ndim)
print(arr.nbytes) #nbytes

import numpy as np
arr=np.array([2,3,1,4,7,8,5,6])
print(arr.argmax())#returns  index of max value
print(arr.argmin())#returns  index of min value
print(arr.argsort())#returns  indexes of values to be sorted
print(np.sort(arr))