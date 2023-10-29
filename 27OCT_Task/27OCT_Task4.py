#Write a Python program to multiply all numbers in a list.
import math
#Method1: product with predefined list
list1=[1,2,3]
product_of_number=math.prod(list1)
print(f"The sum of given numbers in list is:{product_of_number}")
a=input('please enter numbers for the List seperated by comma :\n').split(',')
print(a)
x=list(map(int,a))
#x=[2,1,3,4,5]
y=math.prod(x)
prod=1
for i in range(0,len(x)):
    prod=prod*x[i]
print('The User Input List is\n',x)
print('Product using math Prod function ::\t',y)
print('Product using sort and Index function ::\t',prod)