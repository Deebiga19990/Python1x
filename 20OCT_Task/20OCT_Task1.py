# #palindrome program
# st=input("Enter the string\n")
# j=len(st)-1
# i=0
# flag=1
# while (i<j):
#     if(st[i]==st[j]):
#         print("Hi")
#         i=i+1
#         j=j-1
#         flag=0
#
#     else:
#         flag=-1
#         break
# if(flag==0):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

def is_a_palindrome(a_string):
    a_string = a_string.lower().replace(' ', '')
    return a_string == a_string[::-1]

a_string = input("Enter the string\n")


if is_a_palindrome(a_string)==True:
    print(a_string[::-1])
    print("The given string is a palindrome\n")
else:
    print(a_string[::-1])
    print("The given string is not a palindrome\n")

