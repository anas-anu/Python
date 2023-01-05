while True:
    print("1.RECTANGLE")
    print("2.CIRCLE")
    print("3.CUBOID")
    print("4.SPHERE")

    sel=int(input("PLEASE SELECT A OPERATION:\n"))

    if sel==1:
        from Graphics.rect import*
        l=int(input("Enter the Length of Rectangle:\n"))
        b=int(input("Enter the Breadth of Rectangle:\n"))
        print("Area of Rectangle is:\n",area(l,b))
        print("Perimeter of Rectangle is:\n",perimeter(l,b))
        print("\n")
    elif sel==2:
        from Graphics.circle import*
        r=int(input("Enter the Radius of a Circle:\n"))
        print("Area of Circle is:\n",area(r))
        print("Perimter of Circle is:\n",perimeter(r))
        print("\n")
    elif sel==3:
        from Graphics.graphics.cuboid import*
        l=int(input("Enter the Length of Cuboid:\n"))
        b=int(input("Enter the Breadth of Cuboid:\n"))
        h=int(input("Enter the Height of Cuboid:\n"))
        print("Area of Cuboid is:\n",area(l,b,h))
        print("Perimeter of Cuboid is:\n",perimeter(l,b,h))
        print("\n")
    elif sel==4:
        from Graphics.graphics.sphere import*
        r=int(input("Enter the Radius of a Sphere:\n"))
        print("Area of Sphere is:\n",area(r))
        print("Perimter of Sphere is:\n",perimeter(r))
        print("\n")
    else:
        print("PLEASE SELACT A VALID OPTION")