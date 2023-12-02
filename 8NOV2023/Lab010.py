# Hybrid Inheritance

# multiple types of inheritance, such as single, multiple, and multilevel inheritance.


class A:
    def greet(self):
        print("Method A")

class B:
    def greet(self):
        print("Method B")

class C(A,B):
    pass


class D(B, A):
    pass


obj1 = C()
print(obj1.greet())
obj2 = D()
print(obj2.greet())

print(C.mro())
print(D.mro())

