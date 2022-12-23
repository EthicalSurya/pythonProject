class Digit:
    def __init__(self,dig):
        self.dig=dig

    def __str__(self):              #this method is used print an object here it is 'd'
        return f"The dig is {self.dig}"

    def __len__(self): #This method prints the lenth of an obj here 'd'
        return 1

d=Digit(2)
print(d)
print(len(d))