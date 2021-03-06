#!/usr/bin/python3
"""How many instances with a tracker"""


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates instance with attributes width and height
        Args:
            width: width of the rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Finds the area of a rectangle
        Returns:
            Current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Finds the perimeter of a rectangle
        Returns:
           Current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Prints a rectangle with the # character of .__size"""
        if self.__width == 0 or self.height == 0:
            return("")
        else:
            for col in range(self.__height - 1):
                print(str(self.print_symbol) * self.__width)
            return (str(self.print_symbol) * self.width)

    def __repr__(self):
        """Returns official string representation of an instance"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Sets the width of the rectangle
      Args:
          value(int): width of the square
      Raises:
          TypeError: if the width is not an integer
          ValueError: if width is less than zero
      """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle
        Args:
            value(int): height of the square
        Raises:
            TypeError: if the height is not an integer
            ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
