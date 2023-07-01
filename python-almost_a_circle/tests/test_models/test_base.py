#!/usr/bin/python3
"Task 0"
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_init(unittest.TestCase):
    "Unit test for models/base.py"

    def test_id_right(self):
        base = Base(123)
        self.assertEqual(base.id, 123)

    def test_id_none(self):
        prueba = Base(None)
        self.assertEqual(prueba.id, 4)

    def test_id_2times(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)


class tests_of_JSON_methods(unittest.TestCase):
    "Tests for Json methods"
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file_none(self):
        self.assertEqual(Base.save_to_file(None), None)

    def test_from_json_str_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_load_empty_file(self):
        loaded_list = Base.load_from_file()
        self.assertEqual(loaded_list, [])