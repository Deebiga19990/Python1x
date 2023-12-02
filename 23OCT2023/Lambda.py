#def sayHello():
#     print("Hello")
#
# sayHello()
#
#
# def funcWithParam(a):
#     return a**2
#
# o = funcWithParam(2)
# print(o)

# Lambda Expression -> Now copied by the Java


# def doubleOfMe(value):
#     return value*2


output = lambda value:value*2
print(output(2))


def sayHello(name):
    print("Hi your name is ",name)


sayHelloLambda = lambda name: print("Hi your name is ", name)

sayHello("Pramod")

sayHelloLambda("Lucky")


original_str = "Pramod"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("Pramod") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")



add = lambda x,y : x+y

print(add(3,4))

#lambda without argument
sayhi=lambda:print("HI")
sayhi()

