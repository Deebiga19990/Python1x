# Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character
# are the same.
list2 = []
n = int(input("Enter number of elements in list: \n"))
print(f"Enter {n} numbers\n")
for i in range(0, n):
    val = input()
    list2.append(val)
print(list2)
if len(list2)>=2 and list2[0]==list2[-1]:
    x=len(list2)
    print('The Length of the Strings in a list is ::',x)
else:
    print('The Length of the string is less than 2 or the 1st and last character of the string is not same!!')