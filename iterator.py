'''x=[7,8,9,5]

it=iter(x)

#method 1
print(it.__next__())#7
#method 2
print(next(it)) #8

for i in x:
    print(i)'''

class TopTen:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num +=1

        return val

rep=TopTen()
for i in rep:
    print(i)
