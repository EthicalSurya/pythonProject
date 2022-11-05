f=open("Harry.txt",'r')
print(f.readline())
#f1=f.read() #reads entire file
#f1=f.readline()#reads file line by line
#f1=f.readline(3) # reads first 3 char
#f1=f.readlines() #reads the entire file and returns a list
#print(f.tell()) #returns no of chars
f.seek(6)
print(f.readline())
f.close()

# f=open("Harry Bhai ka code",'rb') #reads in binary
# f1=f.read()
# print(f1)
# f.close()

# f=open("Harry Bhai ka code","r+") # read+write mode
# print(f.read())
# a=f.write("please visit again")
# print(a) #18 no of char written
