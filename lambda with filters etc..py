'''def is_even(n):
    return n%2==0

nums=[2,4,5,7,8,6,9]

evens= list(filter(is_even,nums))

print(evens)''' #without using lambda

from functools import reduce

nums=[2,4,5,7,6,9,8]

evens= tuple(filter(lambda n: n%2==0,nums))
print(evens)

doubles= list(map(lambda n: n*2,evens))
print(doubles)

sum= reduce(lambda a,b:a+b,nums)
print(sum)


