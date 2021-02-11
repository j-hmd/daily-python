# The dataclasses decorator also supports imutable classes
# classes whose value you don't want to change

from dataclasses import dataclass

@dataclass(frozen=True)
class ReferencePoint:
    x: int = 100
    y: int = 200

    def SetPoint(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

p1 = ReferencePoint()
print(p1.x)

# If we try modifying the contents of that class we get an error:
#  File "<string>", line 4, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field 'x'
# p1.x = 10

# And even the class itself can't change its contents when
# the attribute frozen is set to true in the dataclass decorator
# p1.SetPoint(10, 20)
