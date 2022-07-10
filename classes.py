# This file contains the classes and functionality for three shapes:
# Square, Rectangle, and Circle

# Import statements
import math 


class Shape:
    '''Base class for consequent shapes, specifies color'''

    def __init__(self, color: str) -> None:
        self.color = color

        # Set color_rgb attribute based on user input
        if self.color == "black":
            self.color_rgb = (0, 0, 0)
        elif self.color == "white":
            self.color_rgb = (255, 255, 255)
        elif self.color == "red":
            self.color_rgb = (255, 0, 0)
        elif self.color == "blue":
            self.color_rgb = (0, 0, 255)
        elif self.color == "yellow":
            self.color_rgb = (255, 255, 0)
        else:
            # Grey default color
            self.color = "grey"
            self.color_rgb = (128, 128, 128)


class Square(Shape):
    '''Subclass for square with functionality to calculate area and print its equation'''
    def __init__(self, length: int) -> None:
        self.length = length
        self.type = "square"

    def area(length):
        '''Calculates the area of a square'''
        area = length * length
        return area

    def formula():
        '''Prints the equation to calculate the area of a square'''
        equation = "A = a*a"
        return f"The area of a square is calculated by: {equation}"


class Rectangle(Shape):
    '''Subclass for rectangle with functionality to calculate area and print its equation'''
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
        self.type = "rectangle"
    
    def area(length, width):
        '''Calculates the area of a rectangle'''
        area = length * width
        return area

    def formula():
        '''Prints the equation to calculate the area of a rectangle'''
        equation = "A = length * width"
        return f"The area of a rectangle is calculated by: {equation}"


class Circle(Shape):
    '''Subclass for circle with functionality to calculate area and print its equation'''
    def __init__(self, radius: int) -> None:
        self.radius = radius
        self.diameter = radius * 2
        self.type = "circle"

    def area(radius):
        '''Calculates the area of a circle'''
        area = math.pi * radius ** 2
        return area
    
    def formula():
        '''Prints the equation to calculate the area of a circle'''
        equation = "A = pi * radius^2"
        return f"The area of a circle is calculated by: {equation}"

class Cone(Shape):
    '''Subclass for cone with functionality to calculate area and print its equation'''
    def __init__(self, radius: int, height: int) -> None:
        self.radius = radius
        self.height = height
        self.diameter = radius * 2
        self.type = "cone"

    def area(radius, height):
        '''Calculates the area of a cone'''
        area = math.pi * radius * (radius + math.sqrt(height**2+radius**2))
        return area
    
    def formula():
        '''Prints the equation to calculate the area of a cone'''
        equation = "A = πr(r+h2+r2)"
        return f"The area of a cone is calculated by: {equation}"

class Triangle(Shape):
    '''Subclass for triangle with functionality to calculate area and print its equation'''
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height
        self.type = "triangle"

    def area(base, height):
        '''Calculates the area of a triangle'''
        area = 1/2 * base * height
        return area
    
    def formula():
        '''Prints the equation to calculate the area of a triangle'''
        equation = "A = 1/2 * b * h"
        return f"The area of a triangle is calculated by: {equation}"

class Pentagon(Shape):
    '''Subclass for pentagon with functionality to calculate area and print its equation'''
    def __init__(self, perimeter: int, apothem: int) -> None:
        self.perimeter = perimeter
        self.apothem = apothem
        self.type = "pentagon"

    def area(perimeter, apothem):
        '''Calculates the area of a pentagon'''
        area = 1/2 * perimeter * apothem
        return area
    
    def formula():
        '''Prints the equation to calculate the area of a pentagon'''
        equation = "A = 1/2 * p * a"
        return f"The area of a pentagon is calculated by: {equation}"

    


if __name__ == "__main__":
    square = Square("black", 10)
    rectangle = Rectangle("white", 10, 5)
    circle = Circle("blue", 1)
    print("----Square----")
    print("color: ", square.color)
    print("RGB color: ", square.color_rgb)
    print("Area: ", square.area())
    print("Formula: ", square.formula())
    print("--------------")

    print("----Rectangle----")
    print("color: ", rectangle.color)
    print("RGB color: ",rectangle.color_rgb)
    print("Area: ", rectangle.area())
    print("Formula: ", rectangle.formula())
    print("--------------")

    print("----Circle----")
    print("color: ", circle.color)
    print("RGB color: ",circle.color_rgb)
    print("Area: ", circle.area())
    print("Formula: ", circle.formula())
    print("--------------")


