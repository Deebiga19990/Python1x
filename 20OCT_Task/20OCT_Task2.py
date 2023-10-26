def calculate(number):
    print("Actual number is:", number)
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum




number= int(input("Enter a number\n"))
print("sum of digits in given number is",calculate(number),sep=" ")