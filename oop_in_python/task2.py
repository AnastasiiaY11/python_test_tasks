class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

my_rectangle = Rectangle(width=5, height=10)

print(f"Width: {my_rectangle.width}")
print(f"Height: {my_rectangle.height}")