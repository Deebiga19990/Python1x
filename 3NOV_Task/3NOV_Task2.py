# Create a Class Person ,Two Objects by taking (name, age, address)
# Input from users and print details in the end.

class Person:
    Name=None
    Age=None
    Address=None

Object1=Person()
Object1.Name=input("Enter the name\n")
Object1.Age=input("Enter the age\n")
Object1.Address=input("Enter the Address\n")

Object2=Person()
Object2.Name=input("Enter the name\n")
Object2.Age=input("Enter the age\n")
Object2.Address=input("Enter the Address\n")

print("===================Person1_Details===================")
print(f"Person_1 details are Name->{Object1.Name}, Age->{Object1.Age}, Address->{Object1.Address}")

print("===================Person2_Details===================")
print(f"Person_2 details are Name->{Object2.Name}, Age->{Object2.Age}, Address->{Object2.Address}")

