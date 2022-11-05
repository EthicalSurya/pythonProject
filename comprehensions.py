# nums div by 3 below 100 using list comprehension
'''ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)'''

ls=[i for i in range(100) if i%3 is 0] #list comprehension
print(ls)

# Dict comprehension
dict1={i:f"item{i}"for i in range(5)}
print(dict1)
dict2={value:key for key, value in dict1.items()}#swapping key,value
print(dict2)

# nums div by 3 below 100 using set comprehension
s={x for x in range(100) if x%3 is 0}
print(type(s))

# nums div by 3 below 100 using Generator comprehension

gen=(x for x in range(1,100) if x%15 is 0)

for item in gen:
    print(item)