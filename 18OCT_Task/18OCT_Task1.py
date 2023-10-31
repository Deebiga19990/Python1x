#factorial program
number=int(input("Enter the number\n"))
fact=1
if(number<0):
    print("factorial is not possible")
else:
    for number in range(1,number+1):
        fact=fact*number
print(f"factorial of {number} is {fact}")