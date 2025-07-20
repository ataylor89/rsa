def power_mod_n(base, expo, n):
    res = 1
    base = base % n
    while expo > 0:
        if expo & 1:
            res = (res * base) % n
        base = (base * base) % n
        expo = expo // 2
    return res

def encode(cipher, modulus):
    encoding = ""
    size = get_cipher_size(modulus)
    for i in range(0, size):
        encoding += chr(cipher & 0xFF)
        cipher = cipher >> 8
    return encoding

def decode(str):
    cipher = 0
    for i in range(0, len(str)):
        cipher += (ord(str[i]) << 8*i)
    return cipher

def get_cipher_size(modulus):
    k = 1
    while (2**8)**k - 1  < modulus:
        k += 1
    return k
