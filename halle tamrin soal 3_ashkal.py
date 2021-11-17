import math


class Square:
    def __init__(self, size):
        self.size = size
        self.s = 0
        self.p = 0

    def calculate_p(self):
        self.p = self.size * 4
        return self.p

    def calculate_s(self):
        self.s = self.size ** 2
        return self.s

    def __repr__(self):
        return f"s is {self.s} and p is {self.p}"


class Rectangle:
    def __init__(self, tul, arz):
        self.tul = tul
        self.arz = arz
        self.s = 0
        self.p = 0

    def calculate_p(self):
        self.p = 2 * (self.tul + self.arz)
        return self.p

    def calculate_s(self):
        self.s = self.tul * self.arz
        return self.s

    def __repr__(self):
        return f"s is {self.s} and p is {self.p}"


class Triangle:
    def __init__(self, ghaede, ertefa):
        self.ghaede = ghaede
        self.ertefa = ertefa
        self.s = 0
        self.p = 0

    def calculate_p(self):
        vatar = math.sqrt(self.ghaede ** 2 + self.ertefa ** 2)
        self.p = self.ghaede + self.ertefa + vatar
        return self.p

    def calculate_s(self):
        self.s = (self.ghaede * self.ertefa)/2
        return self.s

    def __repr__(self):
        return f"s is {self.s} and p is {self.p}"


s = Square(4)
s.calculate_p()
s.calculate_s()
print(s)
r = Rectangle(3, 4)
r.calculate_p()
r.calculate_s()
print(r)
t = Triangle(3,4)
t.calculate_p()
t.calculate_s()
print(t)
