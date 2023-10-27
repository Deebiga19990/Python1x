#Right angle star pyramid

n = int(input("enter the number to form pyramid:\n"))
for i in range(n):
    for j in range(i+1):
          print("*",end=" ")
    print("")