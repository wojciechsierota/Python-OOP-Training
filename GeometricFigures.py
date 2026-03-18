import math

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.area = 0

    def calculate_area(self):
        self.area = self.side_a * self.side_b
        return self.area
    
    def __str__(self):
        return f"Area: {self.area}"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        self.area = self.side_a ** 2
        return self.area


class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
        self.volume = 0
        
    def calculate_area(self):
        self.area = (self.side_a ** 2) * 6
        return self.area
    
    def calculate_volume(self):
        self.volume = self.side_a ** 3
        return self.volume 

    def __str__(self):
        return f"Cube surface area: {self.area}, Volume: {self.volume}"


class Circle: 
    def __init__(self, radius):
        self.radius = radius
        self.area = 0

    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area
    
    def __str__(self):
        return f"Circle area: {self.area:.2f}"


# --- TEST SCENARIO ---
rect = Rectangle(4, 5)
rect.calculate_area()
print(rect)

sq = Square(5)
sq.calculate_area()
print(sq)

cu = Cube(5)
cu.calculate_area() 
cu.calculate_volume() 
print(cu)

circ = Circle(5)
circ.calculate_area()
print(circ)