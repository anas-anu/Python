n=int(input("Enter a Limit:\n"))
a=0
b=1
res=0
print("Fibonacci Series Up to",n,"Number is:\n")
print(a)
print(b)
res=a+b
while res <= n:
     print(res)
     a = b
     b = res
     res = a + b

