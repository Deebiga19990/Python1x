number=int(input("Enter the number\n"))
first=0
second=1
c=0
for c in range(0,number):
    if(c<=1):
        fibonicci=c
    else:
        fibonicci=first+second
        first=second
        second=fibonicci
    print(fibonicci,end= ' ')
