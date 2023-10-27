#function to do x^y
def power_function(x,y):
    return(x**y)
x=int(input("Enter the base Number\n"))
y=int(input("Enter the power Number\n"))
result=power_function(x,y)
print(f"{x} raised to the power of {y} is {result}")

#Lambda expression to triple power the number
number=int(input("Enter the Number\n"))
triple_the_number = lambda digit:digit**3
print(triple_the_number(number))