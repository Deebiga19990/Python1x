#Write a program that calculates and displays the letter
# grade for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
score=float(input("Enter student's score\n"))
if score>=90 and score<=100:
    print("Grade A")
elif score>=80 and score<=89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score >= 0 and score <= 59:
    print("Grade F")

print("Leap Year Program")
#Create a program that determines whether a given year is a leap year.
year=int(input("Enter the year\n"))
if(year%4==0)and(year%100!=0):
    print(year,"is a leap year\n")
elif (year % 400== 0):
    print(year, "is a leap year\n")
else:
    print(year, "is not a leap year\n")

print("----Triangle Check----")
side1=float(input("Enter the length of side1\n"))
side2=float(input("Enter the length of side2\n"))
side3=float(input("Enter the length of side3\n"))
if(side1==side2)and(side2==side3):
    print("The triangle is equilateral")
if (side1 == side2) or (side2 == side3) or (side1 == side3):
        print("The triangle is isosceles")
if (side1 != side2) and (side2 != side3) and (side1 != side3):
        print("The triangle is scalene ")
