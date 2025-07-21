# RSA Encryption

## Introduction

This repository contains an open-source implementation of the RSA encryption algorithm.

There is a lot to talk about, like the difference between symmetric key cryptography and asymmetric key cryptography, and what public key cryptography is all about.

I'll tell you, in advance, that RSA encryption is a form of asymmetric key cryptography.

In symmetric key cryptography, the encryption key is identical to the decryption key.

In asymmetric key cryptography, the encryption key is different from the decryption key.

Public key cryptography is really just a special case of asymmetric key cryptography.

In public key cryptography, we call the encryption key "public" and the decryption key "private".

Later on in this document, we will give some use cases for RSA encryption.

The RSA algorithm is a powerful form of cryptography because it can be used to send secret messages between two trusted parties, and it can also be used to send secret messages to a corporate server.

If we are sending secret messages to a corporate server, we do not want to send them our private key, so we upload our public key instead.

RSA encryption is based on prime numbers.

The keys that we generate are based on prime numbers.

If we choose very large prime numbers, then it is difficult to derive the private key from the public key.

So even if our public key gets discovered, it is still difficult to derive the private key from the public key, if we base our public key and our private key on large prime numbers, and if we set a long key length, like 1024.

It takes a lot of background to understand these concepts, so we will explain these concepts step-by-step.

First let's discuss the design of our project. After that we will explain the vocabulary that we use.

Then we can really talk about RSA encryption in depth.

We can talk about the algorithm we use to generate a public key and a private key.

We can talk about the algorithm we use to encrypt a message or decrypt an encrypted message.

We can talk about the steps that we take to make RSA encryption secure.

Just remember... we are not obliged to call our encryption key "public".

We can really consider both our encryption key and our decryption key "private".

We can find a secure way to send our encryption key to a trusted party, and still consider it private, because the trusted party keeps it a secret.

If the encryption key is actually discovered by an untrusted paty, then it is still difficult to derive the decryption key from the encryption key, if we use very large prime numbers to generate our keys.

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

## Examples of symmetric key cryptography and asymmetric key cryptography

In my Github I actually have three examples of symmetric key cryptography.

The XOR, rot13, and rot88 algorithms are examples of symmetric key cryptography.

In symmetric key cryptography, the encryption key is identical to the decryption key.

The XOR algorithm is very secure if we choose a randomly generated key with a very long key length (like 1024, 2048, or 4096 bytes).

The rot13 and rot88 algorithms are not secure.

In my Github I currently have one example of asymmetric key cryptography.

The RSA algorithm is an example of asymmetric key cryptography.

In asymmetric key cryptography, the encryption key is different from the decryption key.

The RSA algorithm is very secure if we base our keys on large prime numbers, choose a long key length, and keep both our encryption key and our decryption key a secret.

The RSA algorithm actually has an advantage over the XOR algorithm.

If we use the XOR algorithm and our key gets discovered by an untrusted party, then our messages can be decrypted by the untrusted party, since the XOR algorithm uses the same key for encryption and decryption.

If we use the RSA algorithm and our public key gets discovered by an untrusted party, then it is still very difficult for the untrusted party to decrypt our messages, because it is difficult to derive the private key from the public key, provided that we base our keys on large prime numbers and choose a long key length.

We can use both the XOR and the RSA encryption algorithms to send secret messages between two trusted parties.

If we have to send secret messages to a corporate server, then it is preferrable to use the RSA encryption algorithm. This way, if an untrusted party discovers our public key, it is still very difficult for the untrusted party to decrypt our messages, since it is very difficult to derive the private key from the public key.
