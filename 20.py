l1=[]
n=int(input("ENTER A LIMIT:\n"))
print("Enter Elements:\n")
for i in range(0,n):
    e=int(input())
    l1.append(e)
print(l1)
for i in l1:
    if(i%2==0):
        l1.remove(i)
print("New List is:\n",l1)
