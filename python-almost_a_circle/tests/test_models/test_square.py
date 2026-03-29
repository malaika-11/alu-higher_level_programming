#!/usr/bin/python3
"""Unit tests for Square class."""

import io
import unittest
from contextlib import redirect_stdout
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square behavior and methods."""

    def test_square_one_exists(self):
        """Test direct Square(1) initialization."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_size_type_error(self):
        """Test Square("1") raises TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_x_type_error(self):
        """Test Square(1, "2") raises TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_y_type_error(self):
        """Test Square(1, 2, "3") raises TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_size_negative(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_x_negative(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_y_negative(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_size_zero(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_init(self):
        """Test Square initialization with defaults."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_str(self):
        """Test __str__ format for Square."""
        s = Square(5, 1, 2, 9)
        self.assertEqual(str(s), "[Square] (9) 1/2 - 5")

    def test_size_setter(self):
        """Test size setter updates width and height."""
        s = Square(3)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_error(self):
        """Test size setter raises TypeError for invalid type."""
        s = Square(3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_value_error(self):
        """Test size setter raises ValueError for invalid value."""
        s = Square(3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_display(self):
        """Test display inherited behavior with offsets."""
        s = Square(2, 1, 1)
        stream = io.StringIO()
        with redirect_stdout(stream):
            s.display()
        self.assertEqual(stream.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Test update with positional args for Square."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {
            "id": 10,
            "size": 2,
            "x": 3,
            "y": 4,
        })

    def test_update_kwargs(self):
        """Test update with keyword args for Square."""
        s = Square(1)
        s.update(size=7, y=1, x=2, id=89)
        self.assertEqual(s.to_dictionary(), {
            "id": 89,
            "size": 7,
            "x": 2,
            "y": 1,
        })

    def test_update_args_priority(self):
        """Test args have priority over kwargs."""
        s = Square(1)
        s.update(5, 6, x=99)
        self.assertEqual(s.x, 0)

    def test_to_dictionary(self):
        """Test square dictionary representation."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(
            s.to_dictionary(),
            {"id": 1, "size": 10, "x": 2, "y": 1},
        )


if __name__ == "__main__":
    unittest.main()
