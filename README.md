# RSA Encryption

## Introduction

This repository contains an open-source implementation of the RSA encryption algorithm.

In this readme file, we will attempt to:

1. Teach the RSA encryption algorithm
2. Make the implementation understandable
3. Teach bit arithmetic (left shift, right shift, and, or, xor, not, et cetera)
4. Teach modular arithmetic
5. Explain the difference between symmetric key cryptography and asymmetric key cryptography
6. Explain the concept of public key cryptography

It helps to have a background in the Python programming language, since all of the code is in Python.

Python is a very powerful programming language.

Python allows you to accomplish complex tasks in a short amount of code.

Before we get into the details of RSA encryption, we will explain the design of our project, and define some of the words that we use.

We will also give some examples of symmetric key cryptography and asymmetric key cryptography.

RSA encryption is a form of asymmetric key cryptography.

RSA encryption is also a form of public key cryptography.

Public key cryptography is a special case of asymmetric key cryptography, and we will explain this later on.

## Design

The project is organized into many modules. A module is a Python file.

We describe each module in detail below.

Module | Description
------ | -----------
primetable.py | Creates a prime table of the first n primes for any positive integer n
keytable.py | Generates keys using the prime table
keygen.py | Creates a key pair in publickey.txt and privatekey.txt using the key table
parser.py | Parses publickey.txt or privatekey.txt to return a list of (n, e) or (n, d) pairs
util.py | Contains a utility function power_mod_n which is used in encryption and decryption
encrypt.py | Encrypts a message using the public key
decrypt.py | Decrypts an encrypted message using the private key

## Vocabulary

Throughout this document, and throughout this project, we use a lot of computer science vocabulary.

Let's define some of the words that we use.

Word | Definition
---- | ----------
Algorithm | A list of instructions
Asymmetric key cryptography | A form of cryptography where the encryption key is different from the decryption key
Cipher | An encryption algorithm; also, an encrypted message
Ciphertext | An encrypted message; encrypted information
Code | A code is a language
Decode | To turn code into intelligible data (e.g. decoding a text file means turning numeric data into text)
Deserialize | Reconstruct an object from a series of bytes
Encode | To turn intelligible data into code (e.g. character encoding means turning characters into code points)
Filter | A device that separates an input stream into two categories (what gets filtered in and what gets filtered out)
Key table | A database of keys; a dictionary of keys
Module | In the context of Python, a module is a Python file
Mod/modulo | A binary operation that takes two operands a and b and returns the remainder when a is divided by b
Parser | A parser breaks a word, sentence, or file into parts; a parser breaks a whole into parts; etymology: Latin "pars, partis" which means part or parts
Plaintext | An unencrypted message; unencrypted information
Prime number | A positive integer that is only divisible by 1 and itself
Prime table | A database of primes; a list of primes
Public key cryptography | A special case of asymmetric key cryptography where the encryption key is called "public"and the decryption key is called "private"
Serialize | Convert an object and its data into a series of bytes
Sieve | A sieve is a filter; the kitchen colander is a type of sieve
Symmetric key cryptography | A form of cryptography where the encryption key is identical to the decryption key
Symmetry | Two things are symmetrical if they're the same in some way
Table | Table is really just a synonym for database (a table can be a list, a map, a MySQL table, etc); a table is a database

## Examples

In my Github I have three examples of symmetric key cryptography.

The [XOR](https://github.com/ataylor89/Math2025/tree/main/xor), [ROT13](https://github.com/ataylor89/Math2025/tree/main/rot13), and [ROT88](https://github.com/ataylor89/Math2025/tree/main/rot88) algorithms are examples of symmetric key cryptography.

In my Github I currently have one example of asymmetric key cryptography.

The [RSA algorithm](https://github.com/ataylor89/rsa) is an example of asymmetric key cryptography.
