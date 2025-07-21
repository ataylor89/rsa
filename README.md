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
Prime number | A positive integer greater than one that is only divisible by 1 and itself
Prime table | A database of primes; a list of primes
Public key cryptography | A special case of asymmetric key cryptography where the encryption key is called "public"and the decryption key is called "private"
Serialize | Convert an object and its data into a series of bytes
Sieve | A sieve is a filter; the kitchen colander is a type of sieve
Symmetric key cryptography | A form of cryptography where the encryption key is identical to the decryption key
Symmetry | Two things are symmetrical if they're the same in some way
Table | Table is really just a synonym for database (a table can be a list, a map, a MySQL table, etc); a table is a database
The fundamental theorem of arithmetic | The FTOA states that every positive integer greater than one has a unique prime factorization

## Examples

In my Github I have three examples of symmetric key cryptography.

The [XOR](https://github.com/ataylor89/Math2025/tree/main/xor), [ROT13](https://github.com/ataylor89/Math2025/tree/main/rot13), and [ROT88](https://github.com/ataylor89/Math2025/tree/main/rot88) algorithms are examples of symmetric key cryptography.

In my Github I currently have one example of asymmetric key cryptography.

The [RSA algorithm](https://github.com/ataylor89/rsa) is an example of asymmetric key cryptography.

## Asymmetric versus symmetric

In asymmetric key cryptography, the encryption key is different from the decryption key.

In symmetric key cryptography, the encryption key is identical to the decryption key.

In a secure asymmetric key algorithm, if our public key is discovered, it is still very difficult to derive the private key from the public key.

This is one advantage of asymmetric key cryptography.

This is one advantage of the RSA algorithm.

In a secure symmetric key algorithm, if our key is discovered by an untrusted party, then the untrusted party can use our key to decrypt our messages, since the encryption key is identical to the decryption key.

For this reason, asymmetric key cryptography is often preferred when we have to send secret messages to a corporate server.

The RSA algorithm can be used to exchange secret messages between two trusted parties.

The RSA algorithm can also be used to send and receive secret messages with a corporate server.

## Public key cryptography

Alice and Barbara are best friends and they want to exchange secret messages.

They know there's a risk that someone will discover their encryption key.

For this reason, they use public key cryptography.

If an untrusted party discovers their public key, it is still very difficult for the untrusted party to derive the private key and decrypt the encrypted messages.

Alice uses a program called keytable to create a database of keys.

She then uses a program called keygen to generate a public key and a private key.

Barbara does the same.

Alice gives Barbara her public key. Barbara gives Alice her public key.

Alice uses Barbara's public key to encrypt her messages.

Barbara uses her private key to decrypt Alice's messages.

Barbara uses Alice's public key to encrypt her messages.

Alice uses her private key to decrypt Barbara's messages.

In this way, Alice and Barbara communicate securely via public key cryptography.

If an untrusted party reads their messages, they won't be able to understand the messages, because the messages are encrypted.

If an untrusted party discovers Alice's public key or Barbara's public key, they still won't be able to read the messages, because they have to derive the private key from the public key in order to decrypt the communications.

You can see that public key cryptography is very useful.

In this example, Alice and Barbara use public key cryptography to communicate in a secure way.

Let's describe another scenario.

Suppose Alice wants to send and receive secret messages with a corporate server.

Alice can send the corporate server her public key.

The corporate server can send Alice its public key.

Alice uses the server's public key to encrypt her messages.

The server uses its private key to decrypt her messages.

The server uses Alice's public key to encrypt its messages.

Alice uses her private key to decrypt the server's messages.

In this way, Alice is able to communicate securely with a corporate server.

If an untrusted party reads one of her messages, they won't be able to understand it, because the message is encrypted.

If an untrusted party discovers Alice's public key, or the server's public key, they still will not be able to understand the messages, because they have to derive the private key from the public key in order to decrypt the communications.

One of the main goals of public key cryptography is to make the key pair so secure that it is difficult to derive the private key from the public key.

To do this, the keys are based on very large prime numbers.

We can actually base the keys on prime numbers that are unfathomably large, to make it as secure as possible.

We can base the keys on prime numbers that are over a thousand digits long.

If we do this, the encrypted message will be quite large, because the modulus is very large.

(The modulus is the product of the two prime numbers.)

But listen... that's okay.

It's okay if our encrypted message is very large.

If we really need to, we can decrypt the message character by character, to use as little memory as possible.

This might sound extreme, but if we want to make public key cryptography very secure, we can really use extremely large prime numbers, prime numbers that are over 1000 digits long.

In my experience, I have used prime numbers that are over 1,000,000 in value.

The prime numbers I use are 7 digits long or longer.

I keep on pushing myself to use larger and larger prime numbers, by generating keys on AWS cloud.

I use the infrastructure of AWS cloud to generate very large keys that are hard to crack.

## To be clear

To be clear, I just want to say, public key cryptography is a form of asymmetric key cryptography.

We can say that public key cryptography is a form of asymmetric key cryptography... an example of asymmetric key cryptogtraphy... and also an application of asymmetric key cryptography.

Public key cryptography really falls under the category of asymmetric key cryptography.

In public key cryptography, we say that our encryption key is public and our decryption key is private.

Even though we call our encryption key "public", we still keep it as secret as possible.

We don't just advertise our public key to the whole wide world.

We keep both our public key and our private key as secret as possible.

We can share our public key with a trusted party.

We can create a public key to share with a corporate server.

But we still keep our public key and our private key as secret as possible.

## Secure algorithms versus insecure algorithms

The RSA algorithm is very secure, provided that we base our keys on large prime numbers, choose a large key length (a large number of n-e pairs and n-d pairs), and keep our public key and our private key as secret as possible.

The XOR algorithm is also very secure, provided that we choose a randomly generated key of a long enough length, like 1024 bytes, 2048 bytes, or 4096 bytes.

One advantage of the RSA algorithm is that... if our public key is discovered, it is still very difficult to derive the private key from the public key and decrypt the encrypted messages.

If we use the XOR algorithm, and our key is discovered, a hacker can use our key to decrypt the encrypted messages, because the same key is used for encryption and decryption.

You can see that both the RSA and the XOR algorithms are very secure, but the RSA algorithm has an advantage.

Now it's important to point out... the rot13 and rot88 algorithms are not secure.

ROT13 and ROT88 are known rotation ciphers.

A hacker can try the rot13 and rot88 algorithms on any encrypted message, and see if they have any luck.

It is good to know the rot13 and rot88 rotation ciphers.

Rotation ciphers have been used for thousands of years.

The RSA and XOR algorithms are mathematically very advanced...

The RSA algorithm is based on prime numbers.

The XOR algorithm is based on bit arithmetic and the XOR operation.

Rotation ciphers are mathematically less advanced.

Rotation ciphers were used in classical antiquity.

So it's good to know about rotation ciphers like rot13 and rot88.

But rot13 and rot88 are not secure.

The RSA and the XOR algorithms, on the other hand, are very secure.

The RSA and the XOR algorithms are very secure, provided that you take the appropriate precautions.

## What is the RSA algorithm?

The RSA algorithm is a form of asymmetric key cryptography.

The RSA algorithm is also a form of public key cryptography.

The RSA algorithm is based on a series of (n, e, d) tuples... so we can also call it the NED algorithm.

n is the product of two prime numbers, preferrably, two very large prime numbers.

e is the encryption exponent. d is the decryption exponent.

The RSA algorithm consists of many parts.

These parts are the following:

1. An algorithm for generating a public key and a private key
2. An algorithm for encrypting a message using the public key
3. An algorithm for decrypting an encrypted message using the private key

In the sections that follow, we will explain all three of these parts.
