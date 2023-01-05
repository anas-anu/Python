n=int(input("Enter a Limit:\n"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    i=i+1
print("Factorial Up to",n,"Numbers is:\n",fact)
    