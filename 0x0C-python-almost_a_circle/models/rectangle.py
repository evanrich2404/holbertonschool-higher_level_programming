#!/usr/bin/python3
"""Rectangle class"""
base = __import__('base').Base


class Rectangle(base):
"""Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area"""
        return self.width * self.height
    
    def display(self):
        """display"""
        placeholder = '\n' * self.y
        placeholder += (' ' * self.x + '#' * self.width + '\n') * self.height
        placeholder = placeholder[:-1]
        print(placeholder)
    
    def __str__(self):
        """str"""
        holderofplace = "[Rectangle] " + "({}) ".format(self.id)
        holderofplace += "{}/{} - ".format(self.x, self.y)
        holderofplace += "{}/{}".format(self.width, self.height)
        return holderofplace

    def update(self, *args, **kwargs):
        """update"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary"""
        chicken = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return chicken
