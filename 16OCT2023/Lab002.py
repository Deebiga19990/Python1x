x=int(input("Enter the first number\n"))
y=int(input("Enter the second number\n"))
z=int(input("Enter the third number\n"))
#Max_Value=x
if(x>y and x>z):
    print(f"{x} is greater than {y} and {z}")
elif(y>z):
    print(f"{y} is greater than {x} and {z}")
else:
    print(f"{z} is greater than {x} and {y}")
