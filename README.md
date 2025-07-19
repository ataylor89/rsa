# RSA Encryption

## Introduction

This repository contains an open-source implementation of the RSA encryption algorithm.

RSA encryption is based on prime numbers.

First we generate a prime table from which we can choose prime numbers.

We set a minimum threshold, tmin, and a maximum threshold, tmax.

Then we choose two random prime numbers, p and q, such that p != q and tmin <= p, q <= tmax.

Now we let n = p * q.

If our minimum threshold is high enough, then it is very difficult to factor n without knowing p and q.

However, there's a caveat.

There are some very powerful libraries, like sympy, that are very good at factoring numbers.

If you write your own factorization method, then it might take a long time to factor n.

But if you use sympy, you can factor n very quickly.

So you see that... the difficulty of factoring n is only one part of RSA security.

There's a second part.

We actually generate e and d values for each n value.

The algorithm for generating e and d follows:

1. Choose a minimum threshold tmin and a maximum threshold tmax
2. Choose two random prime numbers p and q such that p != q and tmin <= p, q <= tmax
3. Let n = p * q
4. Let phi be the least common multiple of p-1 and q-1, that is, phi = lcm(p-1, q-1)
5. Let e be the first integer such that 1 < e < phi and gcd(e, phi) == 1, where gcd is the greatest common divisor function
6. Let d be the first integer such that 1 < d < phi and d * e == 1 (mod phi), where mod is the modulo operator
7. Store (n, p, q, phi, e, d) as a key in our key table

You can see that this is not just an algorithm for generating e and d.

It is actually an algorithm for generating keys and storing them in our key table.

If we are going to generate 10 keys between a minimum threshold tmin and a maximum threshold tmax, then we just repeat steps one through seven until we have added 10 new keys to our key table.

Now... we have already discussed the difficulty of factoring n when p and q are large prime numbers.

It is difficult to factor n by hand, and it is even difficult to factor n programmatically...

But using a powerful library like sympy, it is fairly easy to factor n.

There is another security feature in RSA encryption.

It is actually difficult to derive d if you only know n and e.

This statement actually requires additional explanation.

The public key is a series of (n, e) pairs, whereas the private key is a series of (n, d) pairs.

If you know n and e, it is difficult to derive d, when n is very large.

So if we choose very large values for p and q, then n will be very large, since n is the product of p and q.

If n, p, and q are all very large, then it is difficult to derive d knowing n and e.

In other words, it is difficult to derive the private key if you know the public key, provided that our values for n, p, and q are all very large.

That's the whole point of RSA encryption.

Knowing the public key (n and e) it is difficult to derive the private key (n and d) if n is very large.

Unfortunately, it is easy for a supercomputer to crack our code.

Even if we have an unfathomably large n value, which is the product of unfathomably large p and q values, it is still possible for a supercomputer to crack our code.

A supercomputer is so powerful that it can derive n and d given n and e, even if n is very large.

In other words, a supercomputer is so powerful that it can derive our private key given our public key, even if our public key contains very large n values.

So RSA encryption is somewhat secure, but it's not actually secure.

We can say that RSA encryption is semi-secure.

If you encrypt a message using the RSA algorithm, then it might be hard for most hackers to decrypt it.

But if you give a hacker a supercomputer, then they can decrypt your message using the memory and processing power of a supercomputer.

So... the RSA algorithm can be cracked by a supercomputer.

But it's somewhat secure... it's semi-secure... it is difficult for most hackers to decode.

It is definitely worth knowing the RSA algorithm, because it teaches you about prime numbers.

And honestly, if you generate an unfathomably large n value, the product of unfathomably large p and q values, then it is probably the case that 99% of hackers won't be able to decrypt it.

It's only the 1% of hackers who have access to a supercomputer, who will be able to decrypt it.

I want my reader to have no illusions about the security of the RSA encryption algorithm.

The RSA encryption algorithm can be cracked by a supercomputer, but it's so cool, and so interesting, and so based on prime numbers, that it's actually worthwhile to know.

Not only that... it gives you a lot of insight into public key cryptography.

Is there a more secure form of public key cryptography?

That's a good question -- it's a question that I have to research.

In general, the most secure encryption algorithm is a composite encryption algorithm... an encryption algorithm composed of multiple encryption algorithms.

## A philosophical question

There is a really interesting question in philosophy... is the RSA encryption algorithm secure?

Well, if we have access to a supercomputer, then we can often crack an RSA encryption algorithm.

But what if the prime numbers p and q are unimaginably large?

What if p and q are so large, they are unfathomably large?

Then n is unfathomably large, and it is extremely difficult to derive d knowing n and e.

So it is a really interesting question in philosophy... is the RSA encryption algorithm secure?

We can actually choose prime numbers p and q that are so large... they don't even fit on your hard drive.

Then it is really difficult to crack the code.

## Design

Before we talk about how to use the files in this repository, let's quickly discuss the project design.

The project is organized into many modules. A Python file is a module.

Below we describe each module in detail.

Module | Description
------ | -----------
primetable.py | Creates a prime table of the first n primes for any positive integer n
keytable.py | Generates keys using the prime table
keygen.py | Creates a key pair in publickey.txt and privatekey.txt using the key table
parser.py | Parses publickey.txt or privatekey.txt to return a list of (n, e) or (n, d) pairs
util.py | Contains a utility function power_mod_n which is used in encryption and decryption
encrypt.py | Encrypts a message using the public key
decrypt.py | Decrypts an encrypted message using the private key
