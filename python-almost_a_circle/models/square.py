#!/usr/bin/python3
"""Module that defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square with size, position, and optional id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size and propagate to width/height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return formatted square representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Assign square attributes via args or kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for index, value in enumerate(args):
                if index < len(attrs):
                    setattr(self, attrs[index], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
