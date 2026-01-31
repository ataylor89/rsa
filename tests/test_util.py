import primetable
import keytable
import keygen
import time
from util import power_mod_n
from unittest import TestCase

class TestUtil(TestCase):

    @classmethod
    def setUpClass(cls):
        primetable.generate(int(1e4))
        keytable.generate(16, 1056, 1200, verbose=False)
        cls.key = keygen.create_key(16, 1056, 1200)

    @classmethod
    def tearDownClass(cls):
        primetable.table.clear()
        keytable.table.clear()

    def test_power_mod_n(self):
        msg = 'hello world! today is saturday january 31 2026'
        key = self.key
        keylen = len(key)
        
        codepoints = list(map(lambda x: ord(x), msg))
        ciphers = []
    
        for i in range(len(codepoints)):
            n, e, d = key[i % keylen]
            m = codepoints[i]
            c = (m ** e) % n
            cc = power_mod_n(m, e, n)
            assert c == cc
            ciphers.append(c)
    
        for i in range(len(ciphers)):
            n, e, d = key[i % keylen]
            c = ciphers[i]
            m = (c ** d) % n
            mm = power_mod_n(c, d, n)
            assert m == mm

    def test_time_comparison(self):
        msg = 'test'
        key = self.key
        keylen = len(key)

        codepoints = list(map(lambda x: ord(x), msg))
        ciphers = []

        print('Clocking times...')

        for i in range(len(codepoints)):
            n, e, d = key[i % keylen]
            m = codepoints[i]

            start = time.time()
            c = (m ** e) % n
            elapsed1 = time.time() - start

            start = time.time()
            cc = power_mod_n(m, e, n)
            elapsed2 = time.time() - start

            assert c == cc
            ciphers.append(c)

            print(f'({m} ** {e}) % {n} took {elapsed1:.10f} seconds | power_mod_n({m}, {e}, {n}) took {elapsed2:.10f} seconds')

        for i in range(len(ciphers)):
            n, e, d = key[i % keylen]
            c = ciphers[i]

            start = time.time()
            m = (c ** d) % n
            elapsed1 = time.time() - start

            start = time.time()
            mm = power_mod_n(c, d, n)
            elapsed2 = time.time() - start

            assert m == mm

            print(f'({c} ** {d}) % {n} took {elapsed1:.10f} seconds | power_mod_n({c}, {d}, {n}) took {elapsed2:.10f} seconds')
