#condition
age=int(input("Enter  your age\n"))
print(f"Given age is {age}\n")
print("You can watch a movie\n" if age>=18 else "You cant watch a movie\n")

if age>=18:
    print("You can watch a movie\n")
else:
    print("You cant watch a movie\n")
print("--------------")