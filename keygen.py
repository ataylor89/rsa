import keytable
import random
import sys

def create_key_pair(keylen=4):
    if not valid(keylen):
        return None

    publickey = open("publickey.txt", "w")
    privatekey = open("privatekey.txt", "w")

    nvalues = list(keytable.table.keys())
    nvalues = random.sample(nvalues, keylen)

    for nvalue in nvalues:
        (n, p, q, phi, e, d) = keytable.table[nvalue]
        publickey.write("n=%d e=%d\n" %(n, e))
        privatekey.write("n=%d d=%d\n" %(n, d))

    publickey.close()
    privatekey.close()

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
