import primetable
import keytable
import keygen
from util import power_mod_n
from exceptions import KeyLengthError, NotEnoughKeysError
from unittest import TestCase

class TestKeygen(TestCase):

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

    def verify_key(self, keylength, tmin, tmax):
        key = keygen.create_key(keylength, tmin, tmax)
                
        assert len(key) == keylength

        message = "hello world today is friday january 30 2026"

        codepoints = list(map(lambda x: ord(x), message)) 
        ciphers = []

        for i in range(len(codepoints)):
            n, e, d = key[i % keylength]
            m = codepoints[i]
            c = power_mod_n(m, e, n) 
            ciphers.append(c)

        for i in range(len(ciphers)):
            n, e, d = key[i % keylength]
            c = ciphers[i]
            m = power_mod_n(c, d, n)
            assert codepoints[i] == m
            assert message[i] == chr(m)
 
    def test_small_inputs(self):
        with self.assertRaises(KeyLengthError):
            self.verify_key(0, self.tmin, self.tmax)
        self.verify_key(1, self.tmin, self.tmax)
        self.verify_key(2, self.tmin, self.tmax)
        self.verify_key(3, self.tmin, self.tmax)

    def test_large_inputs(self):
        self.verify_key(30, self.tmin, self.tmax)
        self.verify_key(31, self.tmin, self.tmax)
        self.verify_key(32, self.tmin, self.tmax)
        with self.assertRaises(NotEnoughKeysError):
            self.verify_key(33, self.tmin, self.tmax)
