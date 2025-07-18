import keytable
import random
import sys

error_cmdline = "Usage: python keygen.py"
error_missing_table = "The key table does not exist"
error_keylen = "The key length exceeds the number of n values in the key table"

def gen_keys(key_len=4):
    if not valid(key_len):
        return None

    nvalues = list(keytable.table['table'].keys())
    nvalues = random.sample(nvalues, key_len)
    keys = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = keytable.table['table'][nvalue]
        keys.append((n, e, d))
    return keys

def save(keys):
    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))

    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

def valid(key_len):
    num_nvalues = len(keytable.table['table'].keys())
    return key_len <= num_nvalues

def main():
    if len(sys.argv) > 2:
        print(error_msg)
        sys.exit(0)

    if len(sys.argv) == 2:
        key_len = int(sys.argv[1])
    else:
        key_len = 4

    if not keytable.load('keytable.pickle'):
        print(error_missing_table)
        sys.exit(0)

    if not valid(key_len):
        print(error_keylen)
        sys.exit(0)

    keys = gen_keys(key_len)
    save(keys)
    
if __name__ == "__main__":
    main()
