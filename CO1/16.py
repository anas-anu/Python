a=input("ENTER A STRING:\n")
b=input("ENTER ANOTHER STRING:\n")
print("First String is:",a)
print("Second String is:",b)
a1=b[:1]+a[1:]
b1=a[:1]+b[1:]
print("After Swap:",a1," ",b1)
