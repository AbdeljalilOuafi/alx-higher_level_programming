#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """The Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num >= 0 for num in position):
            raise ValueError("position elements must be positive integers")

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError("position elements must be positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.size):
                print("#", end="" if j < self.size - 1 else "\n")
