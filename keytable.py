import primetable
import util
import math
import pickle
import sys
import os
import random
import time

flags = {'existing_table_sufficient': False, 'threshold_too_high': False}

test_message = "hello world! my name is andrew"

def load(path='keytable.pickle'):
    global table
    if os.path.exists(path):
        file = open(path, "rb")
        table = pickle.load(file)
        return True
    return False

def save(path):
    if table and not flags['existing_table_sufficient']:
        file = open(path, "wb")
        pickle.dump(table, file)
        return True
    return False

def generate(s, t):
    global table

    load("keytable.pickle")

    if 'table' in globals() and table['threshold'] >= t and len(table['table']) >= s:
        flags['existing_table_sufficient'] = True
        return True
 
    if 'table' not in globals():
        table = {'threshold': t, 'table': {}}

    primetable.load("primetable.pickle")
    ptablesize = primetable.size()
    startindex = -1
    
    for i in range(0, ptablesize):
        if primetable.get(i) >= t:
            startindex = i
            break

    if startindex == -1:
        flags['threshold_too_high'] = True
        return False

    while not done(s, t):
        i = random.randint(startindex, ptablesize-1)
        j = random.randint(startindex, ptablesize-1)

        if i == j:
            continue

        p = primetable.get(i)
        q = primetable.get(j)
        n = p * q

        print("n = %d, p = %d, q = %d" %(n, p, q))

        if n in table['table']:
            continue

        phi = math.lcm(p-1, q-1)

        print("phi = %d" %phi)

        e = 0
        for e in range(2, phi):
            if math.gcd(e, phi) == 1:
                break

        print("e = %d" %e)

        d = 0
        for d in range(2, phi):
            if (d * e) % phi == 1:
                break

        print("d = %d" %d)

        if test(n, e, d):
            print("Adding key (n=%d, p=%d, q=%d, phi=%d, e=%d, d=%d)" %(n, p, q, phi, e, d))
            table['table'][n] = (n, p, q, phi, e, d)

    flags['existing_table_sufficient'] = False
    flags['threshold_too_high'] = False
    return True

def done(s, t):
    count = 0
    for k in table['table'].keys():
        (n, p, q, phi, e, d) = table['table'][k]
        if p >= t and q >= t:
            count += 1
    return count >= s

def test(n, e, d):
    codes = list(map(lambda x: ord(x), test_message))

    encrypted = []
    for i in range(0, len(codes)):
        encrypted.append(util.power_mod_m(codes[i], e, n))

    decrypted = []
    for i in range(0, len(codes)):
        decrypted.append(util.power_mod_m(encrypted[i], d, n))

    return codes == decrypted

def main():
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python keytable.py <size> <threshold>")
        sys.exit(0)

    size = int(sys.argv[1])
    threshold = int(sys.argv[2])
    
    generate(size, threshold)

    if flags["existing_table_sufficient"]:
        print("The existing table is sufficient")
    elif flags["threshold_too_high"]:
        print("The threshold is too high")
    else:
        save("keytable.pickle")
        print("Created a key table with %d keys that meet threshold %d in %s seconds"
                %(size, threshold, time.time() - start_time))

if __name__ == "__main__":
    main()
