
class Rectangle:
    def __init__(self):
        self.__l=int(input("Enter The Length:\n"))
        self.__w=int(input("Enter The Width:\n"))
    def __lt__(self,x):
        a1=self.__l * self.__w
        a2=x.__l * x.__w
        print("Area Of Rectangle One is:",a1)
        print("Area Of Rectangle Two is:",a2)
        return a1<a2
print("Enter Length And Width of First Rectangle:\n")
r1=Rectangle()
print("Enter Length And Width of Second Rectangle:\n")
x=Rectangle()
if(r1<x):
    print("Lesser Is First Rectangle:")
elif(r1>x):
    print("Lesser Is Secound Rectangle:")
else:
    print("Both are Equal")
    
