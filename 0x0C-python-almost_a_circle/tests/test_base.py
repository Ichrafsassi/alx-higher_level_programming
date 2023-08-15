#!/usr/bin/python3
"""Unittest for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from ast import literal_eval


class TestBaseClass(unittest.TestCase):
    """test Base class """

    def test_id_increasing(self):
        """test Base calss without arguments"""
        base_2 = Base()
        self.assertEqual(base_2.id, 1)
        base_1 = Base(25)
        self.assertEqual(base_1.id, 25)
        base_3 = Base()
        self.assertEqual(base_3.id, 2)

    def test_to_json_string(self):
        """test to json string"""
        rectangle = Rectangle(10, 7, 2, 8)
        dictionary = rectangle.to_dictionary()
        # get json string
        json_dictionary_string = Base.to_json_string([dictionary])
        # convet it to Dict
        json_dictionary = literal_eval(json_dictionary_string[1: -1])
        self.assertDictEqual(dictionary, json_dictionary)
