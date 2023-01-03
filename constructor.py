class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
a=int(input("Enter The Length oF First Rectangle:\n"))
b=int(input("Enter The Breadth oF First Rectangle:\n"))
y=int(input("Enter The Length oF Secound Rectangle:\n"))
z=int(input("Enter The Breadth oF Secound Rectangle:\n"))
r1=Rectangle(a,b)
r2=Rectangle(y,z)
print("Area Of First Rectangle:\n",r1.area())
print("Area Of Secound Rectangle:\n",r2.area())
if r1.area() > r2.area():
    print("Larger Area Is First Rectangle:\n",r1.area())
elif r1.area() < r2.area():
    print("Larger Area Is Secound Rectangle:\n",r2.area())
else:
    print("Both Are Equal")