#!/usr/bin/env python3

from settings import project_root, default_primetable_size
import pickle
import time
import argparse

table = []

def generate(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError('The generate method accepts a positive integer')
    size = 10 * n
    s = sieve(size)
    while s.count('P') < n:
        size *= 10
        s = sieve(size)
    table.clear()
    table.extend([i for i, j in enumerate(s) if j == 'P'][0:n])

def sieve(size):
    if not isinstance(size, int) or size < 2:
        raise ValueError('The sieve method accepts a positive integer greater than or equal to two')
    arr = ['P'] * size
    arr[0] = 'N'
    arr[1] = 'N'
    for i in range(2, size):
        if arr[i] == 'P':
            j = 2
            while i * j < size:
                arr[i * j] = 'C'
                j += 1
    return arr

def get(n):
    return table[n]

def size():
    return len(table)

def load():
    path = project_root / 'database' / 'primetable.pickle'
    if path.is_file():
        with open(path, 'rb') as file:
            table.clear()
            table.extend(pickle.load(file))

def save():
    path = project_root / 'database' / 'primetable.pickle'
    if len(table) > 0:
        with open(path, 'wb') as file:
            pickle.dump(table, file)

def main():
    parser = argparse.ArgumentParser(prog='primetable.py', description='Generate primes and store them in a prime table')
    parser.add_argument('numberofprimes', type=float, default=default_primetable_size, nargs='?')
    args = parser.parse_args()
    try:
        n = int(args.numberofprimes)
        assert n > 0
    except:
        print('Unable to parse the command-line argument as a positive integer')
        return
    load()
    if len(table) >= n:
        print('The existing table is sufficient')
        return
    st = time.time()
    generate(n)
    te = time.time() - st
    save()
    print('Created a prime table with %d primes in %s seconds' %(n, te))

if __name__ == '__main__':
    main()
