x = 20

if x > 10:   #Nested IF
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
  print("NA")

a = 330
b = 330  #shortHandIF
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 33
b = 200
if b > a:   #if statement with no content, put in the pass statement to avoid getting an error.
   pass

#------While loop with break & continue------
i=1
while i<24:
  print(i)
  if i==7:
    break
  i+=1

i=0
while i<24:
  i += 1
  if i==7:
   continue
  print(i)
  #---------

  i = 1
  while i < 6:
    print(i)
    i += 1
  else:
    print("i is no longer less than 6")

