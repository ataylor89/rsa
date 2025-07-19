import keytable
import random
import sys

def create_key_pair(keylen=4):
    if not valid(keylen):
        return None

    nvalues = list(keytable.table.keys())
    nvalues = random.sample(nvalues, keylen)

    keys = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = keytable.table[nvalue]
        keys.append((n, e, d))

    with open("publickey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d e=%d\n" %(n, e))

    with open("privatekey.txt", "w") as file:
        for (n, e, d) in keys:
            file.write("n=%d d=%d\n" %(n, d))

def valid(keylen):
    return keylen <= len(keytable.table)

def main():
    if len(sys.argv) > 2:
        print("Usage: python keygen.py")
        sys.exit(0)

    if not keytable.load("keytable.pickle"):
        print("The key table does not exist")
        sys.exit(0)

    if len(sys.argv) == 2:
        keylen = int(sys.argv[1])
    else:
        keylen = 4

    if not valid(keylen):
        print("The key length exceeds the number of entries in the key table")
        sys.exit(0)

    create_key_pair(keylen)
    print("Created key pair in publickey.txt and privatekey.txt")
    
if __name__ == "__main__":
    main()
