l1=[]
n=int(input("Enter the Limit:\n"))
print("Enter Elements:\n")
for i in range(n):
    e=int(input())
    l1.append(e)
print(l1)
sum=0
for i in range(0,n):
    sum=sum + l1[i]
    i=i+1
print("Sum of All Elements in List is:\n",sum)
