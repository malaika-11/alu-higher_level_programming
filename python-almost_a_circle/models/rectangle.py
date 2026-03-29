#!/usr/bin/python3
"""Module that defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle with size, position, and optional id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width with type and value validation."""
        self.__validate_integer("width", value)
        self.__validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height with type and value validation."""
        self.__validate_integer("height", value)
        self.__validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Get rectangle x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set rectangle x coordinate with validation."""
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Get rectangle y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set rectangle y coordinate with validation."""
        self.__validate_integer("y", value)
        self.__validate_non_negative("y", value)
        self.__y = value

    @staticmethod
    def __validate_integer(name, value):
        """Validate that value is an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @staticmethod
    def __validate_positive(name, value):
        """Validate that width/height is greater than zero."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def __validate_non_negative(name, value):
        """Validate that x/y is zero or greater."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print rectangle using # considering x and y offsets."""
        if self.y > 0:
            print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return formatted rectangle representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assign attributes via positional args or keyword args."""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for index, value in enumerate(args):
                if index < len(attrs):
                    setattr(self, attrs[index], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
