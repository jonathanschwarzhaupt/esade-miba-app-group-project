# This file contains the classes and functionality for three shapes:
# Square, Rectangle, and Circle


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

    def __init__(self, color: str, length: int) -> None:
        super().__init__(color)
        self.length = length
        self.type = "square"


class Rectangle(Shape):
    
    def __init__(self, color: str, length: int, width: int) -> None:
        super().__init__(color)
        self.length = length
        self.width = width
        self.type = "rectangle"

class Circle(Shape):

    def __inti__(self, color: str, radius:int) -> None:
        super().__init__(color)
        self.radius = radius
        self.diameter = radius*2
        self.type = "circle"


if __name__ == "__main__":
    
