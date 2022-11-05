class stack:
    def __init__(self):
        self.stack=[]
        self.k=0    #setting index

    def is_empty(self):
        return self.stack==[]

    def push(self,data):
        self.stack.insert(self.k,data)
        self.k +=1
        return f"{data} pushed into stack"

    def pop(self):
        self.k -=1
        data=self.stack.pop(self.k)
        return f"{data} popped from stack"
    def stack_size(self):
        return len(self.stack)


st=stack()
print(st.push(9))
print(st.push(8))
print(st.push(7))
print(st.push(5))


print(st.stack_size())

print(st.pop())
print(st.pop())

def fizzBuzz(n):
    for i in range(n):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i%5==0 and i%3!=0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(5)