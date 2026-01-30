import primetable
from primecheck import isprime
from unittest import TestCase

class TestPrimetable(TestCase):

    def verify_table(self, size):
        primetable.generate(size)
        assert primetable.size() == size
        for n in primetable.table:
            self.assertTrue(isprime(n))

    def test_small_primetable(self):
        self.verify_table(100)

    def test_large_primetable(self):
        self.verify_table(int(1e4))

    def test_small_inputs_for_primetable(self):
        with self.assertRaises(ValueError):
            primetable.generate(0)
        self.verify_table(1)
        self.verify_table(2)

    def test_negative_input_for_primetable(self):
        with self.assertRaises(ValueError):
            primetable.generate(-1)

    def verify_sieve(self, size):
        sieve = primetable.sieve(size)
        sieve_length = len(sieve)
        assert sieve_length == size
        for i in range(sieve_length):
            if i == 0 or i == 1:
                assert sieve[i] == 'N'
            elif isprime(i):
                assert sieve[i] == 'P'
            else:
                assert sieve[i] == 'C'

    def test_small_sieve(self):
        self.verify_sieve(100)

    def test_large_sieve(self):
        self.verify_sieve(int(1e4))

    def test_small_inputs_for_sieve(self):
        with self.assertRaises(ValueError):
            sieve = primetable.sieve(0)
        with self.assertRaises(ValueError):
            sieve = primetable.sieve(1)
        self.verify_sieve(2)
        self.verify_sieve(3)

    def test_negative_input_for_sieve(self):
        with self.assertRaises(ValueError):
            sieve = primetable.sieve(-1)
