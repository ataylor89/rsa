import pickle
import sys
import os
import time

flags = {'existing_table_sufficient': False}

def get(n):
    return table[n]

def size():
    return len(table)

def load(path='primetable.pickle'):
    global table
    if os.path.exists(path):
        file = open(path, "rb")
        table = pickle.load(file)
        return True
    return False

def save(path='primetable.pickle'):
    global table
    if table and not flags['existing_table_sufficient']:
        file = open(path, "wb")
        pickle.dump(table, file)
        return True
    return False

def generate(n):
    global table

    if load('primetable.pickle') and len(table) >= n:
        flags['existing_table_sufficient'] = True
        return

    size = 10 * n
    s = sieve(n, size)
    while s.count('P') < n:
        size *= 10
        s = sieve(n, size)
    
    table = [i for i, j in enumerate(s) if j == 'P'][0:n]
    flags['existing_table_sufficient'] = False

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

def main():
    start_time = time.time()
    error_msg = "Usage: python primetable.py <numberofprimes>"

    if len(sys.argv) != 2:
        print(error_msg)
        sys.exit(0)

    try:
        n = int(sys.argv[1])
    except:
        print(error_msg)
        sys.exit(0)

    if n <= 0:
        print(error_msg)
        sys.exit(0)
 
    generate(n)

    if flags["existing_table_sufficient"]:
        print("Existing table is sufficient")
    else:
        save("primetable.pickle")
        print("Created a prime table with %d primes in %s seconds" %(n, time.time() - start_time))

if __name__ == "__main__":
    main()
