import primetable
import keytable
import keygen
import encrypt
import decrypt
from tests import test_data_path
from unittest import TestCase

class TestEncryption(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.primetable_size = int(1e4)
        cls.keytable_size = 32
        cls.tmin = 1056
        cls.tmax = int(1e4)
        primetable.generate(cls.primetable_size)
        keytable.generate(cls.keytable_size, cls.tmin, cls.tmax, verbose=False)

    @classmethod
    def tearDownClass(cls):
        primetable.table.clear()
        keytable.table.clear()

    def test_message(self):
        with open(test_data_path / 'message.txt', 'r') as file:
            message = file.read()
        key = keygen.create_key(self.keytable_size, self.tmin, self.tmax)
        ciphertext = encrypt.encrypt(message, key)
        plaintext = decrypt.decrypt(ciphertext, key)
        assert message == plaintext

    def test_specialchars(self):
        with open(test_data_path / 'specialchars.txt', 'r') as file:
            specialchars = file.read()
        key = keygen.create_key(self.keytable_size, self.tmin, self.tmax)
        ciphertext = encrypt.encrypt(specialchars, key)
        plaintext = decrypt.decrypt(ciphertext, key)
        assert specialchars == plaintext
