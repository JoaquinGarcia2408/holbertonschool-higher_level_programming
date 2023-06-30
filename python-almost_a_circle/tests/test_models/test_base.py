#!/usr/bin/python3
"Task 0"
import unittest
from models.base import Base


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