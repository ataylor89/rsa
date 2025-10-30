#!/usr/bin/env python3

import os
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
    home_dir = os.path.expanduser("~")
    default_key = f"{home_dir}/keys/rsa.txt"
    argparser = argparse.ArgumentParser(prog="encrypt.py", description="Encrypt a message")
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument("message", type=str, nargs="?")
    group.add_argument("-m", "--msgfile", type=str)
    argparser.add_argument("-k", "--keyfile", type=str, default=default_key)
    argparser.add_argument("-o", "--output", type=str)
    args = argparser.parse_args()
    if args.msgfile:
        with open(args.msgfile, "r") as msgfile:
            msg = msgfile.read()
    else:
        msg = args.message
    key = parser.parse_key(args.keyfile)
    ciphertext = encrypt(msg, key)
    if args.output:
        outfile = open(args.output, "w")
        outfile.write(ciphertext)
    else:
        print(ciphertext, end="")

if __name__ == "__main__":
    main()
