class Shape:
    def __init__(self, length=0):
        self.length = length

    def calculate_area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calculate_area(self):
        if self.length > 0:
            return self.length ** 2
        else:
            return "Length must be greater than zero!"


squareBig = Square(5)
print(squareBig.calculate_area())
