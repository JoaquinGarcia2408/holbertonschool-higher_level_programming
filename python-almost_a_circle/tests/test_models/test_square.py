#!/usr/bin/python3
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import unittest


class Test_init(unittest.TestCase):
    "Instantiation tests"
    def test_is_subOf_Base(self):
        self.assertIsInstance(Square(5), Base)

    def test_is_subOf_Rectangle(self):
        self.assertIsInstance(Square(7), Rectangle)

    def test_one_and_only_arg(self):
        s5 = Square(10)
        s6 = Square(20)
        self.assertEqual(s5.id, s6.id - 1)

    def test_two_args(self):
        s1 = Square(10, 10)
        s2 = Square(20, 20)
        self.assertEqual(s1.id, s2.id - 1)

    def testing_width_access(self):
        with self.assertRaises(AttributeError):
            Square(10).__width

    def testing_height_access(self):
        with self.assertRaises(AttributeError):
            Square(10, 10).__height

    def testing_x_access(self):
        with self.assertRaises(AttributeError):
            Square(10, 20, 30).__x

    def testing_y_access(self):
        with self.assertRaises(AttributeError):
            Square(10, 20, 30, 40).__y

    def test_setters_validations(self):
        with self.assertRaises(TypeError):
            Square(10).size = "9"

    def test_setters_validations_2(self):
        with self.assertRaises(ValueError):
            Square(10).size = 0


class tests_update(unittest.TestCase):
    "Tests cases for update square"

    def test_pos_args(self):
        sq = Square(10)
        sq.update(1, 2, 3, 4)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.size, 2)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)

    def test_kw_args(self):
        s = Square(10)
        s.update(id=89, size=48, x=82, y=99)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 48)
        self.assertEqual(s.x, 82)
        self.assertEqual(s.y, 99)
