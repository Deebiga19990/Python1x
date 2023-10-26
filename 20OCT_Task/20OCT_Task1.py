#palindrome program
st=input("Enter the string\n")
j=len(st)-1
i=0
flag=1
while (i<j):
    if(st[i]==st[j]):
        print("Hi")
        i=i+1
        j=j-1
        flag=0

    else:
        flag=-1
        break
if(flag==0):
    print("Palindrome")
else:
    print("Not a palindrome")