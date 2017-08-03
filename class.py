
class A:
    def __init__(self, a):
        self.a = a
        print self.a

    def square(self):
        print self.a ** 2


class B(A):
    def squares(self):
        print self.a ** 3


b = B(3)
b.square()
b.squares()
