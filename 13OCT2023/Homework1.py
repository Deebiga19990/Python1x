#use Terenary operator to find max of 3 numbers
x=int(input("Enter the first number\n"))
y=int(input("Enter the second number\n"))
z=int(input("Enter the third number\n"))
Max_Value=x if(x>y and x>z) else y if(y>z) else z
print("Max of", x, y, z ,"is", Max_Value)

#develop the python script the calculates square and cube of given number
a=int(input("Enter the number\n"))
square=a**2
cube=a**3
print(f"square of {a} is {square}")
print(f"cube of {a} is {cube}")

