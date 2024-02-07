#!/usr/bin/python3
class Square:
    """
    class square with an attribute:
        size
    some attributes are protected
    """

    def __init__(self, size=0):
        """
        the initialization function for the square class
        checks for input errors in size
        """
        if type(size) ==int
            self.__size = size
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an Integer")
