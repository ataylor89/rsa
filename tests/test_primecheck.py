from primecheck import isprime
from unittest import TestCase

class TestPrimecheck(TestCase):

    def test_zero_through_ten(self):
        self.assertFalse(isprime(0))
        self.assertFalse(isprime(1))
        self.assertTrue(isprime(2)) # prime
        self.assertTrue(isprime(3)) # prime
        self.assertFalse(isprime(4))
        self.assertTrue(isprime(5)) # prime
        self.assertFalse(isprime(6))
        self.assertTrue(isprime(7)) # prime
        self.assertFalse(isprime(8))
        self.assertFalse(isprime(9))
        self.assertFalse(isprime(10))

    def test_negatives(self):
        self.assertFalse(isprime(-1))
        self.assertFalse(isprime(-2))

    def test_large_primes(self):
        self.assertTrue(isprime(541))
        self.assertTrue(isprime(7919))
        self.assertTrue(isprime(104729))
        self.assertTrue(isprime(1299709))

    def test_large_composites(self):
        self.assertFalse(isprime(267417))
        self.assertFalse(isprime(616363))
        self.assertFalse(isprime(787267))
        self.assertFalse(isprime(847366))

    def test_non_integers(self):
        self.assertFalse(isprime(3.14159))
        self.assertFalse(isprime(2.71828))
