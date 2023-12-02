name="prakalya"
#not possible. Srtings in python are inmutable
# name[0]='A'
result =name.capitalize()
print(name.capitalize())
print(result)
print(name)

#id is built in function. It returns the address/reference
print(id(name))
print(id(name))
print(id(result))
# Upper Case
result2 = name.upper()
print(result2)

# Lower
result3 = name.lower()
print(result3)
print(id(result3))  # Identity - Address Ref.

# Swapcase()
# Returns a copy of the string with uppercase characters converted to lowercase
# and vice versa.

name = "aRvin"
print(name.swapcase())

# Title
# Returns a titlecased version of the string,
# where words start with an uppercase character and
# the remaining characters are lowercase.

name = "hello world"
print(name.capitalize())
print(name.title())
t1 = "dutta ji"
t2 = "pramod ji"
print(t1.capitalize())
print(t2.upper())


name = "Prakalya"
print(len(name))

# Replace
text = "hello world"
#result_rep = text.replace("world","Python")
print(text.replace("world","python"))

#find()
#Returns the lowest index of a substring in the string.
# Returns -1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)
#count() - count the char -
count = text.count("l")
print(count)
count = text.count("a")

print(count)

name  = "p d"
print(len(name))

name  = "pramod"
print(name)
del name
print(name)