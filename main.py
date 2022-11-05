# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''a=[1,2,3,5,7]

n=int(input("enter no for search"))

if n in a:
    print(a.index(n))
else:
    print("invalid search")'''

def names(lst):
    count=0
    for i in lst:
        if len(i)>5:
            count +=1
    return count


lst=['suryam','ramesh','madhu','sai']
c=names(lst)
print(c)

def add(a,b):
    res=a+b
    return res

def mul(a,b):
    prod=a*b
    print(prod)

res=add(5,6)
#print(bes)
prod=mul(5,5)
print(prod)







