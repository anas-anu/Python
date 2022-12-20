a={ }
b={ }
nf=int(input("Enter Dictionary Length of First: \n"))
for i in range(0,nf):
    key=input("Enter Key:\n")
    value=input("Enter Values:\n")
    a[key]=value
print(a)
ns=int(input("Enter Dictionary Length of Second: \n"))
for i in range(0,ns):
    key=input("Enter Key:\n")
    value=input("Enter Values:\n")
    b[key]=value
print(b)
a.update(b)
print("Merged Dictionary is: ",a)
