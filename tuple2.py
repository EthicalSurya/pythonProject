fruits = ("apple", "banana", "cherry") # This is packing
print(fruits)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # This is unpacking

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits # adding * to the variable name and the values will be assigned to the variable as a list:

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "mango", "papaya")
for i in fruits:
    print(i)

fruits = ("apple", "mango", "papaya")
for i in range(len(fruits)):
    print(fruits[i])

fruits = ("apple", "mango", "papaya")
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #joiningTuplesByMul
print(mytuple)
