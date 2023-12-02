val = None
name = None
# None is not the same as False.
# None is not an empty string.
# None is not 0.

a = None
b = None

#val = None + 2
# unsupported operand type(s) for +: 'NoneType' and 'int'
print(val)
#error - print(len(val)) #object of type 'NoneType' has no len()
name = "pramod"
print(name)
print (type(val)) #<class 'NoneType'>
print(id(val))

# print(len(val)) # print(len(val)) this is not possible