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

## A different way to think about RSA encryption

Throughout this document we have used the terms public key and private key.

We have also used the term "public key cryptography".

But there is a different way to think about RSA encryption.

We can use a different terminology.

Instead of using the terms "public key" and "private key", we can use the terms "encryption key" and "decryption key".

Instead of using the term "public key cryptography", we can use the term "asymmetric key cryptography".

It turns out that public key cryptography is just a special case of asymmetric key cryptography.

We can keep our encryption key private, just like we keep our decryption key private.

Sometimes we only want the other party to know our encryption key.

We can find a secure way to send the other party our encryption key.

Sometimes we want the other party to know both our encryption key and our decryption key.

We can find a secure way to send the other party our encryption key and our decryption key.

In both of these cases, the encryption key is not "public", because we found a secure way to share it with a trusted party and the trusted party keeps it a secret.

So if we keep our encryption key and our decryption key a secret, then the RSA algorithm is very secure.

To enhance the security of our algorithm, we can use a very long key length... like a key length of 1024.

A key length of 1024 means that the encryption key contains 1024 (n, e) tuples and the decryption key contains 1024 (n, d) tuples.

If we keep both the encryption key and the decryption key a secret, and we use an appropriate key length, like 1024, then the RSA algorithm is just as secure as the XOR algorithm that we implemented in a separate project.

I think that's fair to say...

I think it's fair to say that... if we keep both our keys a secret, and we use an appropriate key length, like 1024, then the RSA algorithm is as secure as the XOR algorithm.

The main difference between the RSA algorithm and the XOR algorithm is that the RSA algorithm is an example of asymmetric key cryptography, whereas the XOR algorithm is an example of symmetric key cryptography.

In my Gitub I have given three examples of symmetric key cryptography: xor, rot13, and rot88.

I have given one example of asymmetric key cryptography: RSA.

It is really useful to learn about asymmetric key cryptography and symmetric key cryptography.

The RSA algorithm is an example of asymmetric key cryptography, because the encryption key is different from the decryption key.

The XOR, rot13, and rot88 algorithms are three examples of symmetric key cryptography, because the encryption key is identical to the decryption key.

Public key cryptography is just a special case of asymmetric key cryptography.

If we call our encryption key "public", we are implying that it has a high degree of visibility.

But we don't have to call our encryption key "public".

We can say that our encryption key is private just like our decryption key.

We can keep both keys private, and find a secure way to share one or both with a trusted party.

We can set a long key length, like 1024.

If we follow these precautions, then the RSA algorithm is just as secure as the XOR algorithm.

If we keep both our keys private and use a long key length, then the RSA algorithm is very secure.

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
