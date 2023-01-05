n=int(input("Enter a Limit:\n"))
l1=[]
l2=[]
print("Enter Words:\n")
for i in range(0,n):
    e=str(input())
    l1.append(e)
print("The List is:\n",l1)
for i in range(0,n):
    a=len(l1[i])
    l2.append(a)
l2.sort()
print("Length of the largest Word is:\n",l2[-1])

    
    
    