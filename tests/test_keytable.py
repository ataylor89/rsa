import primetable
import keytable
import math
from unittest import TestCase

class TestKeytable(TestCase):

    @classmethod
    def setUpClass(cls):
        primetable.generate(int(1e4))

    def verify_table(self, numkeys, tmin, tmax):
        keytable.generate(numkeys, tmin, tmax, verbose=False)
        for (n, p, q, phi, e, d) in keytable.table.values():
            assert n == p * q

            assert phi == math.lcm(p-1, q-1)

            ee = 0
            for ee in range(2, phi):
                if math.gcd(ee, phi) == 1:
                    break
            assert e == ee

            dd = 0
            for dd in range(2, phi):
                if (dd * ee) % phi == 1:
                    break
            assert d == dd
        keytable.table.clear()

    def test_generate(self):
        self.verify_table(8, 1056, int(1e4))
