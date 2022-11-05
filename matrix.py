def matrix(m,n):
    O=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"enter O[{i}][{j}]"))
            row.append(inp)
        O.append((row))
    return O

def sum(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            s=A[i][j]+B[i][j]
            row.append(s)
        output.append(row)
    return output



m=int(input("enter no of rows"))
n=int(input("enter no of cols"))
print("Enter matrix A")
A=matrix(m,n)
print(A)
print("Enter matrix B")
B=matrix(m,n)
print(B)
s=sum(A,B)
print(s)