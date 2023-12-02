def func():
    name = "Pramod"
    return name

def func2():
    name = "Pramod"
    name #python doesnt throw error even if variable is simply used

# Is this function return anything?

# output = func()
output = func()
print(output)
output = func2()
print(output)


num = 20

def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return num



op = multiply_by_10(num)
print(op)
print("Value of num outside function:", num)