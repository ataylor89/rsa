import pickle
import sys
import os
import time

table = []

def generate(n):
    if len(table) >= n:
        return False
    size = 10 * n
    s = sieve(n, size)
    while s.count('P') < n:
        size *= 10
        s = sieve(n, size)
    table.clear()
    table.extend([i for i, j in enumerate(s) if j == 'P'][0:n])
    return True

def sieve(n, size):
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

def load(path='primetable.pickle'):
    if os.path.exists(path):
        with open(path, "rb") as file:
            table.clear()
            table.extend(pickle.load(file))

def save(path='primetable.pickle'):
    if len(table) > 0:
        with open(path, "wb") as file:
            pickle.dump(table, file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python primetable.py <numberofprimes>")
        return
    try:
        n = int(sys.argv[1])
        assert n > 0
    except:
        print("Unable to parse n as a positive integer")
        return
    load()
    st = time.time()
    modified = generate(n)
    te = time.time() - st
    if modified:
        save()
        print("Created a prime table with %d primes in %s seconds" %(n, te))
    else:
        print("The existing table is sufficient.")

if __name__ == "__main__":
    main()
