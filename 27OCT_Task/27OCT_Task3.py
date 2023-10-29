#Write a Python program to sum all numbers in a list.
#Method1: Sum with predefined list
list1=[3,7,9,1,6,9,22,17]
sum_of_number=sum(list1)
print(f"The sum of given numbers in list is:{sum_of_number}")

#Method2: To sum with run time user list
list2 = []
n = int(input("Enter number of elements : \n"))
print(f"Enter {n} numbers\n")
for i in range(0, n):
    val = int(input())
    list2.append(val)
print(list2)
sum_of_number=sum(list2)
print(f"The sum of given numbers in list is:{sum_of_number}")

#Method3: To sum with user defined function
def sum1(num):
    sum2=0
    for i in range(0, len(num)):
        sum2 +=num[i]
    return sum2

list3=[3,7,9,1,6,9,22,17]
sum_of_number=sum(list3)
print(f"The sum of given numbers in list is:{sum_of_number}")

