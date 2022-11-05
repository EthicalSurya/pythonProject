import numpy as np
import pandas as pd

a=np.array([11,12,13,14])
print(a)
'''x=np.where(a==13) #using where()
print(x)'''
x=np.searchsorted(a,15) #Binary search
print(x)

import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

import numpy as np
arr = np.array([[50, 40, 70],[20,30,80]])
print(np.sort(arr,axis=0))

s="application working properly"
vowels=['a','e','i','o','u']
def filter_str(s):
    for i in s:
        if i in vowels:
            print(i,end='')


'''import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0, 5])
ypoints = np.array([0, 150])

plt.plot(xpoints, ypoints)
plt.show()'''

import numpy as np
data=pd.DataFrame(np.arange(16).reshape(4,4),
            index=['London','Paris','Newyork','Capetown'],columns=['one','two','three','four'])
print(data)

#print(data['two'])
#print(data[['two','three']])

print(data.iloc[1])
print(data.iloc[1,2])#1st row 2nd index
print(data.iloc[1,[1,2]])#1st row 1,2 index
print(data.iloc[[1,2]])#1,2rows

print(data.loc['London'])
print(data.loc['London',['one','two']])


