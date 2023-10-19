a=3
b=3
print(a)
print(a==b)
print(a!=b)
print(a**b)
print(a^b)

#Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pie as 3.14)
#area of circle
r=float(input("Enter the radius\n"))
pi=3.14
area=pi*(r**2)
print("The area of circle is",area)
print("________Another method to import math___________")
import math
r=float(input("Enter the radius\n"))
area=math.pi*(r**2)
print("The area of circle is",area)

#Create a program that takes two numbers as input and prints
#whether the first number is greater than, less than, or equal to the second number.
num1=int(input("Enter number 1\n"))
num2=int(input("Enter number 2\n"))
print("num1 is greater than num2" if(num1>num2) else "num1 is lesser than num2"
if(num1<num2) else "Both number is equal")