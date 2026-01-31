#!/usr/bin/env python3

from settings import project_root, default_tmin, default_tmax
from exceptions import ThresholdError, InsufficientPrimeTableError
import primetable
import util
import math
import pickle
import random
import time
import argparse

table = {}
test_message = 'hello world! my name is andrew'

def generate(numkeys, tmin, tmax, verbose=True):
    if numkeys < 1:
        raise ValueError('The number of keys must be a positive integer')
    if tmin < 0:
        raise ThresholdError('tmin must be a nonnegative integer')
    if tmin > tmax:
        raise ThresholdError('tmin must be less than or equal to tmax')

    count = 0
    startindex = -1
    endindex = -1

    for i in range(primetable.size()):
        if startindex < 0 and primetable.get(i) >= tmin:
            startindex = i
        if endindex < 0 and primetable.get(i) > tmax:
            endindex = i - 1
        if startindex > 0 and endindex > 0:
            break

    if startindex == -1:
        raise InsufficientPrimeTableError('The prime table does not have any primes that meet or exceed the minimum threshold')

    if endindex == -1:
        endindex = primetable.size() - 1

    while count < numkeys:
        i = random.randint(startindex, endindex)
        j = random.randint(startindex, endindex)

        if i == j:
            continue

        p = primetable.get(i)
        q = primetable.get(j)
        n = p * q

        if verbose:
            print('n = %d, p = %d, q = %d' %(n, p, q))

        if n in table:
            continue

        phi = math.lcm(p-1, q-1)

        if verbose:
            print('phi = %d' %phi)

        e = 0
        for e in range(2, phi):
            if math.gcd(e, phi) == 1:
                break

        if verbose:
            print('e = %d' %e)

        d = 0
        for d in range(2, phi):
            if (d * e) % phi == 1:
                break

        if verbose:
            print('d = %d' %d)

        if test(n, e, d):
            if verbose:
                print('Adding key (n=%d, p=%d, q=%d, phi=%d, e=%d, d=%d)' %(n, p, q, phi, e, d))
            table[n] = (n, p, q, phi, e, d)
            count += 1
        elif verbose:
            print(f'The key n={n}, p={p}, q={q}, e={e}, d={d}, phi={phi} did not pass the test')

def test(n, e, d):
    codes = list(map(lambda x: ord(x), test_message))

    encrypted = []
    for i in range(0, len(codes)):
        encrypted.append(util.power_mod_n(codes[i], e, n))

    decrypted = []
    for i in range(0, len(codes)):
        decrypted.append(util.power_mod_n(encrypted[i], d, n))

    return codes == decrypted

def load():
    path = project_root / 'database' / 'keytable.pickle'
    if path.is_file():
        with open(path, 'rb') as file:
            table.clear()
            table.update(pickle.load(file))

def save():
    if len(table) > 0:
        path = project_root / 'database' / 'keytable.pickle'
        with open(path, 'wb') as file:
            pickle.dump(table, file)

def main():
    primetable.load()
    parser = argparse.ArgumentParser(prog='keytable.py', description='Generate (n, e, d) tuples and store them in a key table')
    parser.add_argument('numberofkeys', type=int)
    parser.add_argument('-tmin', '--min_threshold', type=float, default=default_tmin)
    parser.add_argument('-tmax', '--max_threshold', type=float, default=default_tmax)
    args = parser.parse_args()
    numkeys = args.numberofkeys
    tmin = int(args.min_threshold)
    tmax = int(args.max_threshold)
    load()
    st = time.time()
    try:
        generate(numkeys, tmin, tmax)
    except Exception as err:
        print(err)
        return
    te = time.time() - st
    save()
    print('Generated %d keys for tmin=%d and tmax=%d in %s seconds' %(numkeys, tmin, tmax, te))

if __name__ == '__main__':
    main()
