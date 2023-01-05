l1=[ ]
l2=[ ]
a=int(input("ENTER LIMIT OF FIRST LIST: \n"))
print("ENTER ELEMENTS OF FIRST LIST: \n")
for i in range(0,a):
    e=int(input())
    l1.append(e)
print("LIST ONE IS: \n",l1)

b=int(input("ENTER LIMIT OF SECOND LIST: \n"))
print("ENTER ELEMENTS OF SECOND LIST: \n")
for i in range(0,b):
    f=int(input())
    l2.append(f)
print("LIST SECOND IS: \n",l2)
#length check
x=len(l1)
print("Length of List One is: ",x)
y=len(l2)
print("Length of List Second  is: ",y)
if x==y:
    print("BOTH ARE SAME LENGTH")
else:
    print("LIST ARE NOT SAME LENGTH")
#sums same value
sum1=sum2=0
for i in l1:
    sum1+=i
for j in l2:
    sum2+=j
if (sum1==sum2):
    print("LIST SUMS TO SAME VALUE:")
else:
    print("LIST SUMS IS NOT SAME VALUE:")
#common elements
for i in l1:
    for j in l2:
        if (i==j):
            print("COMMON ELEMENTS OCCUR: \n",i)
            break
        else:
            print("COMMON ELEMEMTS NOT OCCUR: \n",i)
            break
        