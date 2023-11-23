
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

super_rectangle = Rectangle(width=5, height=8)
area = super_rectangle.calculate_area()
perimeter = super_rectangle.calculate_perimeter()

print(f"Rectangle Area: {area}")
print(f"Rectangle Perimeter: {perimeter}")
