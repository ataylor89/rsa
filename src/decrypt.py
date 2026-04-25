#!/usr/bin/env python3

from settings import default_key_path
import parser
import util
import argparse
import base64

def decrypt(ciphertext, key):
    bytearr = base64.b64decode(ciphertext)
    message = ''
    keylen = len(key)
    start = 0
    end = 0
    i = 0
    while start < len(ciphertext):
        (n, e, d) = key[i % keylen]
        size = util.size(n)
        end = start + size
        block = bytearr[start:end]
        cipher = int.from_bytes(block, byteorder='big')
        codepoint = util.power_mod_n(cipher, d, n)
        message += chr(codepoint)
        i += 1
        start += size
    return message

def main():
    argparser = argparse.ArgumentParser(prog='decrypt.py', description='Decrypt a message using the RSA algorithm')
    group = argparser.add_mutually_exclusive_group(required=True)
    group.add_argument('ciphertext', type=str, nargs='?')
    group.add_argument('-i', '--inputfile', type=str)
    argparser.add_argument('-k', '--keyfile', type=str, default=default_key_path)
    argparser.add_argument('-o', '--outputfile', type=str)
    args = argparser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'rb') as file:
            ciphertext = file.read()
    else:
        ciphertext = args.ciphertext
    key = parser.parse_key(args.keyfile)
    msg = decrypt(ciphertext, key)
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(msg)
    else:
        print(msg, end='')

if __name__ == '__main__':
    main()
