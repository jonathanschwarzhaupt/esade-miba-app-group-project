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
    def __init__(self, color: str, length: int) -> None:
        super().__init__(color)
        self.length = length
        self.type = "square"

    def area(self):
        '''Calculates the area of a square'''
        area = self.length * self.length
        return area

    def formula(self):
        '''Prints the equation to calculate the area of a square'''
        equation = "A = a*a"
        return f"The area of a square is calculated by: {equation}"

class Rectangle(Shape):
    '''Subclass for rectangle with functionality to calculate area and print its equation'''
    def __init__(self, color: str, length: int, width: int) -> None:
        super().__init__(color)
        self.length = length
        self.width = width
        self.type = "rectangle"
    
    def area(self):
        '''Calculates the area of a rectangle'''
        area = self.length * self.width
        return area

    def formula(self):
        '''Prints the equation to calculate the area of a rectangle'''
        equation = "A = a*a"
        return f"The area of a square is calculated by: {equation}"

class Circle(Shape):
    '''Subclass for circle with functionality to calculate area and print its equation'''
    def __init__(self, color: str, radius: int) -> None:
        super().__init__(color)
        self.radius = radius
        self.diameter = radius * 2
        self.type = "circle"

    def area(self):
        '''Calculates the area of a circle'''
        area = math.pi * self.radius ** 2
        return area
    
    def formula(self):
        '''Prints the equation to calculate the area of a circle'''
        equation = "A = pi * radius^2"
        return f"The area of a circle is calculated by: {equation}"



if __name__ == "__main__":
   
