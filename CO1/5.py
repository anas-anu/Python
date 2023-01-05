n=int(input("Enter Number Of Elements:\n"))
l1=[]
print("Enter Integers:\n")
for i in range(n):
    e=int(input())
    if e>=100:
        l1.append('OVER')
    else:
        l1.append(e)
print("The List Is:\n",l1)