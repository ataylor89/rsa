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
