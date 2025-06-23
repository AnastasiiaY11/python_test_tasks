class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

my_rectangle = Rectangle(width=5, height=10)

rectangle_area = my_rectangle.area()

print(f"The rectangle has a width of {my_rectangle.width} and a height of {my_rectangle.height}.")
print(f"Area: {rectangle_area}")
