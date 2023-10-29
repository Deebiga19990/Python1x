#Write a Python program to find the smallest number in a list
#Min Value with predefined list
list1=[3,7,9,1,6,9,22,17]
min_number=min(list1)
print(f"The smallest number in the list is:{min_number}")

#Min Value with run time user list
list2 = []
n = int(input("Enter number of elements : \n"))
print(f"Enter {n} numbers\n")
for i in range(0, n):
    val = int(input())
    list2.append(val)

print(list2)
min_number=min(list2)
print(f"The smallest number in the list is:{min_number}")

