def area_sqr():
    a=int(input("Enter a Side:\n"))
    x=lambda a:a**2
    print("Area of a Square is:",x(a))
def area_rect():
    w=int(input("Enter Width:\n"))
    l=int(input("Enter Length:\n"))
    x=lambda w,l:w*l
    print("Area of a Rectangle is:",x(w,l))
def area_tri():
    b=int(input("Enter Base:\n"))
    h=int(input("Enter Height:\n"))
    x=lambda b,h:float(0.5)*(b*h)
    print("Area of a Triangle is:",x(b,h))

print("1.AREA OF A SQUARE\n2.AREA OF A RECTANGLE\n3.AREA OF A TRIANGLE\n")
opt=int(input("Choose An Option:\n"))
if opt==1:
    area_sqr()
elif opt==2:
    area_rect()
elif opt==3:
    area_tri()