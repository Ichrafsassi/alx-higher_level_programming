#!/usr/bin/python3
"""Unittest for base class"""

import unittest

from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClassArguments(unittest.TestCase):
    """ test Rectangle class Arguments validation"""

    def test_rectangle_class_inherited_from_base(self):
        """check if is Rectangle class inherited from base or not """
        rectangle = Rectangle(10, 20)
        self.assertEqual(isinstance(rectangle, Base), True)

    def test_argumnets_count(self):
        """test arguments count"""
        with self.assertRaises(TypeError):
            rect4 = Rectangle()
        with self.assertRaises(TypeError):
            rect4 = Rectangle(10, 22, 1, 1, 1, "emad")

    def test_width(self):
        """test width validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)

        rect.width = 15
        self.assertEqual(rect.width, 15)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height(self):
        """test height validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.height, 5)

        rect.height = 15
        self.assertEqual(rect.height, 15)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -5

    def test_x(self):
        """test x validation"""
        rect = Rectangle(10, 5, 1)
        self.assertEqual(rect.x, 1)

        rect.x = 15
        self.assertEqual(rect.x, 15)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y(self):
        """test y validation"""
        rect = Rectangle(10, 5, 1, 20)
        self.assertEqual(rect.y, 20)

        rect.y = 15
        self.assertEqual(rect.y, 15)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5

    def test_area(self):
        """test area"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)


class TestRectangleClassMethods(unittest.TestCase):
    """test Rectangle class methods """
    # test disply method

    def test_display(self):
        """test display method"""

        # Case 1 width < hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(2, 3)
            rectangle.display()
            expected_output = "##\n##\n##\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 width > hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(3, 2)
            rectangle.display()
            expected_output = "###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 width == hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.width = 3
            rectangle.height = 3
            rectangle.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 3 worng number of arguments
        with self.assertRaises(TypeError):
            rectangle.display(2)

    def test_display_useing_x_y(self):
        """test display method using x y"""

        # Case 1 use only x
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(2, 3, 3, 0)
            rectangle.display()
            expected_output = "   ##\n   ##\n   ##\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 use only y
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(3, 2, 0, 3)
            rectangle.display()
            expected_output = "\n\n\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

        # Case 2 useing x, y
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(3, 2, 2, 3)
            rectangle.display()
            expected_output = "\n\n\n  ###\n  ###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

    def test_display_return_none(self):
        """test display return"""
        with patch('sys.stdout', new=StringIO()):
            rectangle = Rectangle(3, 2, 2, 3)
            self.assertIsNone(rectangle.display())

    def test_str(self):
        """test __str__ magic method"""

        rectangle = Rectangle(5, 15, 0, 0, 12)
        # case 1 without x , y
        self.assertEqual(str(rectangle), "[Rectangle] (12) 0/0 - 5/15")

        # case 2 with x , y
        rectangle.x = 5
        rectangle.y = 7
        self.assertEqual(str(rectangle), "[Rectangle] (12) 5/7 - 5/15")

    # test update method
    def test_update_without_args(self):
        """test update method without arguments"""
        rectangle = Rectangle(5, 10, 0, 10, 5)
        old_hight = rectangle.height
        old_width = rectangle.width
        old_x = rectangle.x
        old_y = rectangle.y
        old_id = rectangle.id

        # case 1 dont change anything
        rectangle.update()
        self.assertEqual(old_id, rectangle.id)
        self.assertEqual(old_hight, rectangle.height)
        self.assertEqual(old_width, rectangle.width)
        self.assertEqual(old_x, rectangle.x)
        self.assertEqual(old_y, rectangle.y)

    def test_update_with_args(self):
        """test update method arguments"""
        rectangle = Rectangle(5, 10, 0, 10, 5)
        rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(1, rectangle.id)
        self.assertEqual(2, rectangle.width)
        self.assertEqual(3, rectangle.height)
        self.assertEqual(4, rectangle.x)
        self.assertEqual(5, rectangle.y)

    def test_update_with_args_kwargs(self):
        """test update method args kwargs in this case we have to use args"""
        rectangle = Rectangle(5, 10, 0, 10, 5)

        # case 1 using real attr
        rectangle.update(1, id=2)
        self.assertEqual(1, rectangle.id)

        # case 2 using fake attr
        rectangle.update(1, emad=2)
        self.assertEqual(1, rectangle.id)

    def test_update_with_kwargs(self):
        """test update using kwargs """
        rectangle = Rectangle(10, 10, 10, 10, 5)

        # error
        with self.assertRaises(ValueError):
            rectangle.update(emad=1)
        old_hight = rectangle.height
        old_x = rectangle.x
        old_y = rectangle.y
        rectangle.update(width=1, id=87)
        self.assertEqual(rectangle.id, 87)
        self.assertEqual(old_hight, rectangle.height)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(old_x, rectangle.x)
        self.assertEqual(old_y, rectangle.y)

    # test the to_dictionary method
    def test_to_dictionary(self):
        """test to_dictionary"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_rect_dic = {'height': 2, 'id': 5, 'width': 1, 'x': 3, 'y': 4}
        self.assertDictEqual(rectangle.to_dictionary(), expected_rect_dic)

        with self.assertRaises(TypeError):
            rectangle.to_dictionary(2)
