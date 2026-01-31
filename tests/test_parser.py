import parser
from tests import test_data_path
from exceptions import KeyFileError
from unittest import TestCase

class TestParser(TestCase):

    def valid_key(self):
        path = test_data_path / 'valid_key.txt'
        key = parser.parse_key(path)
        assert len(key) == 64
        for ned in key:
            assert len(ned) == 3

    def valid_key_of_size_one(self):
        path = test_data_path / 'valid_key2.txt'
        key = parser.parse_key(path)
        assert len(key) == 1
        assert len(key[0]) == 3

    def key_with_missing_e_value(self):
        path = test_data_path / 'invalid_key.txt'
        with self.assertRaises(KeyFileError):
            key = parser.parse_key(path)

    def key_with_non_integer_e_value(self):
        path = test_data_path / 'invalid_key2.txt'
        with self.assertRaises(KeyFileError):
            key = parser.parse_key(path)

    def key_with_invalid_line(self):
        path = test_data_path / 'invalid_key3.txt'
        with self.assertRaises(KeyFileError):
            key = parser.parse_key(path)
