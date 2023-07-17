#!/usr/bin/python3
"""Unittest for base class"""

import unittest

from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClassArguments(unittest.TestCase):
    """test Square class Arguments validation """

    def test_square_class_inherited_from_base(self):
        """check if is Square class inherited from base or not """
        square = Square(10)
        self.assertEqual(isinstance(square, Rectangle), True)

    def test_argumnets_count(self):
        """test arguments count"""
        with self.assertRaises(TypeError):
            rect4 = Square()
        with self.assertRaises(TypeError):
            rect4 = Square(10, 22, 1, 1, 1, "emad")

    def test_size(self):
        """test size validation"""
        rect = Square(10)
        self.assertEqual(rect.size, 10)

        rect.size = 15
        self.assertEqual(rect.size, 15)

        with self.assertRaises(TypeError):
            rect.size = "invalid"

        with self.assertRaises(ValueError):
            rect.size = -5

    def test_x(self):
        """test x validation"""
        rect = Square(5, 1)
        self.assertEqual(rect.x, 1)

        rect.x = 15
        self.assertEqual(rect.x, 15)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y(self):
        """test y validation"""
        rect = Square(1, 0, 20)
        self.assertEqual(rect.y, 20)

        rect.y = 15
        self.assertEqual(rect.y, 15)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5

    def test_area(self):
        """test area"""
        rect = Square(10)
        self.assertEqual(rect.area(), 100)

        rect = Square(5)
        self.assertEqual(rect.area(), 25)


class TestSquareClassMethods(unittest.TestCase):
    """test Square class methods """
    # test disply method

    def test_display(self):
        """test display method"""
        # Case 1
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(3)
            square.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2
        with self.assertRaises(TypeError):
            square.display(2)

    def test_display_useing_x_y(self):
        """test display method using x y"""

        # Case 1 use only x
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(2, 3)
            square.display()
            expected_output = "   ##\n   ##\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 use only y
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(2, 0, 3)
            square.display()
            expected_output = "\n\n\n##\n##\n"
            self.assertEqual(expected_output, fake_out.getvalue())

        # Case 2 useing x, y
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(3, 2, 2, 3)
            square.display()
            expected_output = "\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

    def test_display_return_none(self):
        """test display return"""
        with patch('sys.stdout', new=StringIO()):
            square = Square(3, 2, 2, 3)
            self.assertIsNone(square.display())

    def test_str(self):
        """test __str__ magic method"""

        square = Square(5, 15, 0, 12)
        # case 1 without x , y
        self.assertEqual(str(square), "[Square] (12) 15/0 - 5")

        # case 2 with x , y
        square.x = 5
        square.y = 7
        self.assertEqual(str(square), "[Square] (12) 5/7 - 5")

    # test update method
    def test_update_without_args(self):
        """test update method without arguments"""
        square = Square(5, 10, 0, 10)
        old_size = square.size
        old_x = square.x
        old_y = square.y
        old_id = square.id
        # case 1 dont change anything
        square.update()
        self.assertEqual(old_id, square.id)
        self.assertEqual(old_size, square.size)
        self.assertEqual(old_x, square.x)
        self.assertEqual(old_y, square.y)

    def test_update_with_args(self):
        """test update method arguments"""
        square = Square(5, 10, 0, 10)
        square.update(1, 2, 3, 4)
        self.assertEqual(1, square.id)
        self.assertEqual(2, square.size)
        self.assertEqual(3, square.x)
        self.assertEqual(4, square.y)

    def test_update_with_args_kwargs(self):
        """test update method args kwargs in this case we have to use args"""
        square = Square(5, 10, 0, 10)

        # case 1 using real attr
        square.update(1, id=2)
        self.assertEqual(1, square.id)

        # case 2 using fake attr
        square.update(1, emad=2)
        self.assertEqual(1, square.id)

    def test_update_with_kwargs(self):
        """test update using kwargs"""
        square = Square(10, 10, 10, 10)

        # error
        with self.assertRaises(ValueError):
            square.update(emad=1)
        old_x = square.x
        old_y = square.y
        square.update(size=1, id=87)
        self.assertEqual(square.id, 87)
        self.assertEqual(square.size, 1)
        self.assertEqual(old_x, square.x)
        self.assertEqual(old_y, square.y)
