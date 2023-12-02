import keyword
print(keyword.kwlist)
""" 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'"""

#class="Arvin"
#invalid syntex
#cant use keyword as a variable

#variable
#variable name should b unique
name="Arvin"
print(name)
name2="Arvin Madhan"
print(name2)
#string- bunch of character
#char- A,B, a,b etc
#special characters available
x=5
print(type(x))
name="Prakalya"
print(type(name))
y=3.14
print(type(y))
ismale= True
print(type(ismale))
#comple number
cn=3+4j
print(cn)
print(type(cn))

#name=input("Enter your first name")
#name2=input("Enter your last name")
#print(name,name2,sep='-',end="\t")
name3=input("Enter your name")
print("Welcome to class",name3, "for python class")