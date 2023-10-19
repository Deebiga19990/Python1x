side1=float(input("Enter the length of side1\n"))
side2=float(input("Enter the length of side2\n"))
side3=float(input("Enter the length of side3\n"))
if(side1==side2)and(side2==side3):
    print("The triangle is equilateral")
if (side1 == side2) and (side2 != side3):
        print("The triangle is isosceles")
if (side2 == side3) and (side1 != side3):
        print("The triangle is isosceles")
if (side1 == side3) and (side2 != side3):
        print("The triangle is isosceles")
if (side1 != side2) and (side2 != side3) and (side1 != side3):
        print("The triangle is scalene ")