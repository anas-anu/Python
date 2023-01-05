import myfn

a=int(input("Enter First Number: \n"))
b=int(input("Enter Second Number: \n"))

while True:
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.REMINDER")
    sel=int(input("PLEASE SELECT A OPERATION:\n"))
    if sel==1:
        s2=myfn.sumd(a,b)
        print(s2)
    elif sel==2:
         s1=myfn.sub(a,b)
         print(s1)
    elif sel==3:
        s3=myfn.mul(a,b)
        print(s3)
    elif sel==4:
        s4=myfn.div(a,b)
        print(s4)
    elif sel==5:
        s5=myfn.rem(a,b)
        print(s5)
    elif sel>5:
        break





