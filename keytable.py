import primetable
import util
import math
import pickle
import sys
import os

flags = {'existing_table_sufficient': False}

error_msg = "Usage: python keytable.py <size> <threshold>"
existing_table_sufficient = "The existing table is sufficient"

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

def generate(s, t):
    global table

    load("keytable.pickle")

    if 'table' in globals() and table['threshold'] >= t and len(table['table']) >= s:
        flags['existing_table_sufficient'] = True
        return
 
    if 'table' not in globals() or table['threshold'] < t:
        table = {
            'threshold': t,
            'table': {}
        }

    kmin = 0
    primetable.load("primetable.pickle")
    ptablesize = primetable.size()
    
    for i in range(1, ptablesize):
        if primetable.get(i) >= t:
            kmin = i
            break

    for i in range(kmin, ptablesize):
        if len(table['table']) >= s:
            break

        for j in range(kmin, ptablesize):
            if len(table['table']) >= s:
                break

            p = primetable.get(i)
            q = primetable.get(j)
            n = p * q

            if n in table['table']:
                continue

            phi = math.lcm(p-1, q-1)

            e = 0
            for e in range(2, phi):
                if math.gcd(e, phi) == 1:
                    break

            d = 0
            for d in range(2, phi):
                if (d * e) % phi == 1:
                    break

            if test(n, e, d):
                print("Adding key (n=%d, p=%d, q=%d, phi=%d, e=%d, d=%d)" %(n, p, q, phi, e, d))
                table['table'][n] = (n, p, q, phi, e, d)

    flags['existing_table_sufficient'] = False

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
    if len(sys.argv) != 3:
        print(ERROR_MSG)
        sys.exit(0)

    size = int(sys.argv[1])
    threshold = int(sys.argv[2])
    
    generate(size, threshold)

    if flags['existing_table_sufficient']:
        print(existing_table_sufficient)
    else:
        save("keytable.pickle")

if __name__ == "__main__":
    main()
