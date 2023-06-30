#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"Rectangle sub-class unittests"


class Test_init(unittest.TestCase):
    "Test instantiation of Rectangle"

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_only_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_rectangles_id(self):
        rect = Rectangle(8, 4)
        angle = Rectangle(12, 6)
        self.assertEqual(rect.id, angle.id - 1)

    def test_four_args(self):
        rect = Rectangle(8, 4, 0, 1)
        angle = Rectangle(12, 6, 1, 2)
        self.assertEqual(rect.id, angle.id - 1)

    def test_five_args(self):
        rect = Rectangle(8, 4, 0, 0, 7)
        angle = Rectangle(12, 6, 1, 1, 8)
        self.assertEqual(7, rect.id)

    def test_width_getter(self):
        rect = Rectangle(2, 2)
        self.assertEqual(rect.width, 2)

    def test_height_getter(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.height, 3)

    def test_x_getter(self):
        rect = Rectangle(2, 2, 4)
        self.assertEqual(rect.x, 4)

    def test_y_getter(self):
        rect = Rectangle(2, 2, 4, 5)
        self.assertEqual(rect.y, 5)

    def test_width_access(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__width

    def test_height_access(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__height

    def test_x_access(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__x

    def test_y_access(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__y


class test_input_validation(unittest.TestCase):
    "Tests suite for input validation"

    def test_width_notInt(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("Jon", 2)

    def test_height_notInt(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "Snow")

    def test_x_notInt(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "Winterfell")

    def test_y_notInt(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "RedWedding")

    def test_width_underEqual_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_height_underEqual_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_x_under0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -1)

    def test_y_under0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -1)


class test_area(unittest.TestCase):
    "Cases suite for area method of Rectangle"

    def test_base(self):
        rect = Rectangle(10, 10)
        self.assertEqual(rect.area(), 100)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).area(42)

    def test_str_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4).display(2)


class test_update(unittest.TestCase):
    "Test cases for update"

    def test_base_update(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(10, 20, 30, 40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)

    def test_kw_update(self):
        r = Rectangle(1, 1)
        r.update(id=11, height=12, width=13, y=9, x=15)
        self.assertEqual(r.id, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.x, 15)
