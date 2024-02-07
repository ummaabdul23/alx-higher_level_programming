#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if type(size) ==int
            self.__size = size
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an Integer")
