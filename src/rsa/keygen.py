from rsa import default_generated_key_path, primetable, keytable
from rsa.exceptions import KeyLengthError, ThresholdError, NotEnoughKeysError
import random
import argparse

def create_key(keylen, tmin, tmax):
    if keylen < 1:
        raise KeyLengthError('The key length must be a positive integer')
    if tmin < 1056:
        raise ThresholdError('tmin must be greater than or equal to 1056')
    if tmin > tmax:
        raise ThresholdError('tmin must be less than or equal to tmax')
    keytable.load()
    filtered = {}
    for k,v in keytable.table.items():
        if v[1] >= tmin and v[1] <= tmax and v[2] >= tmin and v[2] <= tmax:
            filtered[k] = v
    if keylen > len(filtered):
        raise NotEnoughKeysError('There aren\'t enough keys in the key table that meet the criteria')
    nvalues = list(filtered.keys())
    nvalues = random.sample(nvalues, keylen)
    key = []
    for nvalue in nvalues:
        (n, p, q, phi, e, d) = filtered[nvalue]
        key.append((n, e, d))
    return key

def main():
    primetable.load()
    parser = argparse.ArgumentParser(prog='keygen.py', description='Create a public key and a private key')
    parser.add_argument('keylength', type=int, default=64, nargs='?')
    parser.add_argument('-tmin', '--min_threshold', type=float, default=1056)
    parser.add_argument('-tmax', '--max_threshold', type=float, default=primetable.get(-1))
    parser.add_argument('-o', '--outputfile', type=str, default=default_generated_key_path)
    args = parser.parse_args()
    keylen = args.keylength
    tmin = int(args.min_threshold)
    tmax = int(args.max_threshold)
    try:
        key = create_key(keylen, tmin, tmax)
    except Exception as err:
        print(err)
        return
    with open(args.outputfile, 'w') as file:
        for (n, e, d) in key:
            file.write("n=%d e=%d d=%d\n" %(n, e, d))
        print('Created keyfile %s' %args.outputfile)
    
if __name__ == '__main__':
    main()
