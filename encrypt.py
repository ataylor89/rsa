import parser
import util
import pickle
import sys

def encrypt(msg, key):
    codes = list(map(lambda x: ord(x), msg))
    keylen = len(key)
    cipher = []
    for i in range(0, len(codes)):
        (n, e) = key[i % keylen]
        cipher.append(util.power_mod_n(codes[i], e, n))
    return cipher

def main():
    if len(sys.argv) != 2: 
        print("Usage: python encrypt.py <messagefile>")
        sys.exit(0)

    msgfile = open(sys.argv[1], "r")
    msg = msgfile.read()

    key = parser.parse_key("publickey.txt")
    cipher = encrypt(msg, key)

    cipherfile = open("cipher.txt", "wb")
    pickle.dump(cipher, cipherfile)

if __name__ == "__main__":
    main()
