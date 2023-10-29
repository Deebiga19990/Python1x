#Write a Python program to find the largest number in a list
#Max Value with predefined list
list1=[3,7,9,1,6,9,22,17]
max_number=max(list1)
print(f"The largest number in the list is:{max_number}")

#Max Value with run time user list
list2 = []
n = int(input("Enter number of elements : \n"))
print(f"Enter {n} numbers\n")
for i in range(0, n):
    val = int(input())
    list2.append(val)

print(list2)
max_number=max(list2)
print(f"The largest number in the list is:{max_number}")