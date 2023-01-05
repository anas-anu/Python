import math
l1=[]
n=int(input("Enter the 4 Digit Limit:\n"))
for i in range(1000,n):
    if(math.sqrt(i)==int(math.sqrt(i)) and i%2==0):
        l1.append(i)
print(l1)