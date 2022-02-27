class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append((self.len))

    def print_size(self):
        return ("{} by {} by {} by {}".format(self.len, self.len, self.len, self.len))

    def equal_is(self):
        return squ1 is squ2

squ1 = Square(20)
squ2 = Square(15)
print(Square.square_list)
print(squ1.print_size())
print(squ2.print_size())
print(squ1 is squ2)