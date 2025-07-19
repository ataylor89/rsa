import primetable
import util
import math
import pickle
import sys
import os
import random
import time

flags = {'pmin_too_high': False}

test_message = "hello world! my name is andrew"

def load(path='keytable.pickle'):
    global table
    if os.path.exists(path):
        file = open(path, "rb")
        table = pickle.load(file)
        return True
    return False

def save(path):
    if 'table' in globals():
        file = open(path, "wb")
        pickle.dump(table, file)
        return True
    return False

def generate(numkeys, pmin, pmax):
    global table

    load("keytable.pickle")
    count = 0

    if 'table' not in globals():
        table = {}

    startindex = -1
    endindex = -1

    for i in range(0, primetable.size()):
        if startindex < 0 and primetable.get(i) >= pmin:
            startindex = i
        if endindex < 0 and primetable.get(i) >= pmax:
            endindex = i
        if startindex > 0 and endindex > 0:
            break

    if startindex == -1:
        flags['pmin_too_high'] = True
        return count

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

        print("n = %d, p = %d, q = %d" %(n, p, q))

        if n in table:
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
            table[n] = (n, p, q, phi, e, d)
            count += 1

    flags['pmin_too_high'] = False
    return count

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

    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python keytable.py <numberofkeys> <optional:pmin> <optional:pmax>")
        sys.exit(0)

    primetable.load()
    numkeys = int(sys.argv[1])

    if len(sys.argv) >= 3:
        pmin = int(sys.argv[2])
    else:
        pmin = 0

    if len(sys.argv) == 4:
        pmax = int(sys.argv[3])
    else:
        pmax = primetable.table[-1]
    
    count = generate(numkeys, pmin, pmax)

    if flags["pmin_too_high"]:
        print("pmin is too high")
    else:
        save("keytable.pickle")
        print("Generated %d keys for pmin=%d and pmax=%d in %s seconds"
                %(count, pmin, pmax, time.time() - start_time))

if __name__ == "__main__":
    main()
