#!/usr/bin/python3
"""Square class module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherit from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor method."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a custom string."""
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.width)
        return "[Square] (" + a + ") " + b + "/" + c + " - " + d
