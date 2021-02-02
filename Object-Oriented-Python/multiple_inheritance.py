class A:
    def __init__(self):
        # It seems to be because when we call super from C, it will use MRO to call A's init. But by adding calls to super in A and B, the super method will be the class Object?
        super().__init__()  # not sure why we need this call to super in this case? I guess we're calling the init for object?
        self.foo = "foo"
        self.name = "class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"

# Multiple inheritance: C inherits from A and B
# Python has something called MRO: method resolution order, which is dictated by the order in which we
# create the multiple inheritance. In this case, the order is C, A, B and then Object
class C(A, B):
    def __init__(self):
        super().__init__()

    def ShowAttributes(self):
        print(self.foo)
        print(self.bar)  # Without the super().__init__() in the upper classes, this attribute didn't show...?
        print(self.name)

c = C()
# Both A and B have the same attribute, and that's going to resolve by the method resoluion order
c.ShowAttributes()

# We can print the MRO by using the following:
print(C.__mro__)
# This shows what the order is!