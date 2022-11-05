def add(a,b):
    return a+b
print("the sum is:",add(2,3))

# multiplication of two or more numbers
def multiple(*a):
    result = 1
    for i in a:
        result = result * i
    return result
# insert any number of arguments for multiplication, example:
res = multiple(12, 2, 5)
print(res)
# In this example, code output is = 120

import pandas as pd
l={
    "calaroies":[100,200,300],
    "days":["day1","day2","day3"]
}
var=pd.DataFrame(l)
print(var)