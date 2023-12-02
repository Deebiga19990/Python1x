num = int(input("Enter your Number\n"))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num //= 10  # num = int(num /10)

print(sum)