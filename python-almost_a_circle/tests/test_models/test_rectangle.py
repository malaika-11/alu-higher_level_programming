#!/usr/bin/python3
"""Unit tests for Rectangle class."""

import io
import unittest
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle behavior and methods."""

    def test_rectangle_ids(self):
        """Test id auto-assignment through Base inheritance."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id, r1.id + 1)

    def test_rectangle_attributes(self):
        """Test Rectangle stores width, height, x, and y values."""
        r = Rectangle(5, 6, 1, 2, 9)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 9)

    def test_width_type_error(self):
        """Test width raises TypeError when not integer."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("5", 2)

    def test_height_type_error(self):
        """Test height raises TypeError when not integer."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_x_type_error(self):
        """Test x raises TypeError when not integer."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, "1", 0)

    def test_y_type_error(self):
        """Test y raises TypeError when not integer."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 0, [])

    def test_width_value_error(self):
        """Test width raises ValueError when <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_value_error(self):
        """Test height raises ValueError when <= 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_height_zero_value_error(self):
        """Test Rectangle(1, 0) raises ValueError for height."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_x_value_error(self):
        """Test x raises ValueError when negative."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -1)

    def test_y_value_error(self):
        """Test y raises ValueError when negative."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 0, -1)

    def test_area(self):
        """Test area method returns width * height."""
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_str(self):
        """Test __str__ output format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_offset(self):
        """Test display method prints rectangle without offset."""
        r = Rectangle(2, 3)
        stream = io.StringIO()
        with redirect_stdout(stream):
            r.display()
        self.assertEqual(stream.getvalue(), "##\n##\n##\n")

    def test_display_with_offset(self):
        """Test display method respects x and y offsets."""
        r = Rectangle(2, 2, 1, 1)
        stream = io.StringIO()
        with redirect_stdout(stream):
            r.display()
        self.assertEqual(stream.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Test update method with positional args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {
            "id": 89,
            "width": 2,
            "height": 3,
            "x": 4,
            "y": 5,
        })

    def test_update_kwargs(self):
        """Test update method with keyword args."""
        r = Rectangle(1, 1)
        r.update(height=2, y=3, width=4, x=5, id=90)
        self.assertEqual(r.to_dictionary(), {
            "id": 90,
            "width": 4,
            "height": 2,
            "x": 5,
            "y": 3,
        })

    def test_update_args_priority(self):
        """Test args take precedence over kwargs in update."""
        r = Rectangle(1, 1)
        r.update(10, 2, 3, y=99)
        self.assertEqual(r.to_dictionary()["y"], 0)

    def test_to_dictionary(self):
        """Test to_dictionary output keys and values."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9},
        )


if __name__ == "__main__":
    unittest.main()
