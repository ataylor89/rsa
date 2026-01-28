#!/usr/bin/env python3

import parser
import util
import argparse
import sys

def encrypt(msg, key):
    ciphertext = ''
    codepoints = list(map(lambda x: ord(x), msg))
    keylen = len(key)
    for i in range(len(codepoints)):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        cipher = util.power_mod_n(codepoints[i], e, n)
        encoding = util.encode(cipher, size)
        ciphertext += encoding
    return ciphertext

def main():
    base_dir = sys.path[0]
    default_key = base_dir + '/keys/defaultkey.txt'
    argparser = argparse.ArgumentParser(prog='encrypt.py', description='Encrypt a message using the RSA algorithm')
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument('message', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    argparser.add_argument('-k', '--keyfile', type=str, default=default_key)
    argparser.add_argument('-o', '--outputfile', type=str)
    args = argparser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            msg = file.read()
    else:
        msg = args.message
    key = parser.parse_key(args.keyfile)
    ciphertext = encrypt(msg, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(ciphertext)
    else:
        print(ciphertext, end='')

if __name__ == '__main__':
    main()
