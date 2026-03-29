#!/usr/bin/python3
"""Unit tests for Base class."""

import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def tearDown(self):
        """Clean up generated files after each test."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_id_auto_increment(self):
        """Test automatic id incrementation for Base instances."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        """Test explicit id assignment."""
        b = Base(99)
        self.assertEqual(b.id, 99)

    def test_to_json_string_none(self):
        """Test JSON serialization for None input."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test JSON serialization for empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_data(self):
        """Test JSON serialization for valid dictionary list."""
        data = [{"id": 1, "x": 2}]
        self.assertEqual(Base.to_json_string(data), json.dumps(data))

    def test_from_json_string_none(self):
        """Test JSON deserialization for None input."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test JSON deserialization for empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_data(self):
        """Test JSON deserialization for valid JSON string."""
        data = [{"id": 1, "x": 2}]
        self.assertEqual(Base.from_json_string(json.dumps(data)), data)

    def test_save_to_file_none(self):
        """Test save_to_file with None input writes empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_rectangle_save_to_file_empty(self):
        """Test Rectangle.save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_save_to_file_empty(self):
        """Test Square.save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_and_load_rectangles(self):
        """Test saving rectangles and loading them back."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()

        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[0], Rectangle)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())

    def test_save_and_load_squares(self):
        """Test saving squares and loading them back."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()

        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[1], Square)
        self.assertEqual(loaded[1].to_dictionary(), s2.to_dictionary())

    def test_create_rectangle(self):
        """Test creating Rectangle via dictionary values."""
        data = {"id": 7, "width": 4, "height": 6, "x": 1, "y": 2}
        r = Rectangle.create(**data)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.to_dictionary(), data)

    def test_create_square(self):
        """Test creating Square via dictionary values."""
        data = {"id": 3, "size": 9, "x": 2, "y": 4}
        s = Square.create(**data)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.to_dictionary(), data)

    def test_load_from_file_missing(self):
        """Test load_from_file returns empty list when file missing."""
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
