import parser
import util
import argparse

def encrypt(msg, key):
    ciphertext = ""
    codes = msg.encode("utf-8")
    keylen = len(key)
    for i in range(0, len(codes)):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        cipher = util.power_mod_n(codes[i], e, n)
        encoding = util.encode(cipher, size)
        ciphertext += encoding
    return ciphertext

def main():
    argparser = argparse.ArgumentParser(prog="encrypt.py", description="Encrypt a message")
    argparser.add_argument("-m", "--msgfile", type=str, required=True)
    argparser.add_argument("-k", "--keyfile", type=str, default="key.txt")
    argparser.add_argument("-o", "--output", type=str)
    args = argparser.parse_args()
    msgfile = open(args.msgfile, "r")
    msg = msgfile.read()
    key = parser.parse_key(args.keyfile)
    ciphertext = encrypt(msg, key)
    if args.output:
        outfile = open(args.output, "w")
        outfile.write(ciphertext)
    else:
        print(ciphertext, end="")

if __name__ == "__main__":
    main()
