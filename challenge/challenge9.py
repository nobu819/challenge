class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width + self.len)*2

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, l):
        self.len_a = l + self.len
        print(self.len_a * 4)

class Horse:
    def __init__(self, c, rider):
        self.color = c
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rec = Rectangle(12, 10)
rec.what_am_i()
print(rec.calculate_perimeter())

squ = Square(8)
squ.what_am_i()
print(squ.calculate_perimeter())
squ.change_size(-7)

yutaka = Rider("Take Yutaka")
teio = Horse("brown", yutaka)
print(teio.rider.name)