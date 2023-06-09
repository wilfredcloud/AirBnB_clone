#!/usr/bin/python3
"""This modules defines unittests for file_storage.py

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import unittest
import json
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for instantiation of the FileStorage
    """

    def test_FileStorage_init_no_arg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for FileStorage methods
    """

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))


if __name__ == "__main__":
    unittest.main()
