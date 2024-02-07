#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected.
    """
    def __init__(self, size=0):
        """
        initialization function for the square class
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of square
        """
        return self.__size **
