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
The fundamental theorem of arithmetic | The fundamental theorem of arithmetic states that every positive integer greater than one has a unique prime factorization

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

## Generating a public key and a private key

The algorithm for generating a public key and a private key is described below.

1. Choose a key length. For this example let keylen = 1024.
2. Choose a size for our prime table. For this example let N = 100,000.
3. Generate the first N primes and store them in a prime table.
4. Choose a minimum threshold tmin and a maximum threshold tmax. For this example let tmin=1000 and tmax=10,000.
5. Let count be the number of keys we have generated. At the present moment, count = 0.
6. Choose two distinct primes p and q from our prime table such that tmin <= p <= tmax and tmin <= q <= tmax.
7. Let n = p * q.
8. Let phi be the least common multiple of p-1 and q-1, that is, phi = lcm(p-1, q-1).
9. Let e be the first positive integer such that 1 < e < phi and gcd(e, phi) == 1, where gcd is the greatest common divisor function.
10. Let d be the first positive integer such that 1 < d < phi and d * e == 1 (mod phi).
11. Append "(n, e)\n" to publickey.txt
12. Append "(n, d)\n" to privatekey.txt
13. Increment count by 1, that is, count += 1.
14. If count < keylen then go to step 6; else, continue.
15. We are done! Our public key is stored in publickey.txt and our private key is stored in privatekey.txt.

I forgot to mention that publickey.txt and privatekey.txt start as empty files.

We append (n, e) to publickey.txt and (n, d) to privatekey.txt after we calculate (n, e, d).

We stop when we have generated the required number of keys (i.e. count == keylen).

Our public key is a list of (n, e) tuples and it is stored in the file publickey.txt.

Our private key is a list of (n, d) tuples and it is stored in the file privatekey.txt.

We use the public key to encrypt messages. We use the private key to decrypt encrypted messages.

Now, let's explain the algorithm for encrypting a message using the public key.

## Encrypting a message using the public key

The algorithm for encrypting a message using the public key is described below.

1. Read the message from a file (e.g. message.txt) and store in a variable called message.
2. Parse publickey.txt into a list of (n, e) tuples and store in a variable called key.
3. Let keylen be the length of our public key.
4. Let ciphertext be the variable that stores our encrypted message.
5. Let ord be a function that returns the code point for a Unicode character.
6. Let size(n) be a utility function that calculates the number of bytes needed to store a positive integer n.
7. Let power_mod_n(m, e, n) be a utility function that efficiently calculates m^e % n.
8. Let encode(n, s) be a utility function that encodes a number n as a string of size s.
9. for i = 0, i < lengthof(message), i++
    1. let m = ord(message[i])
    2. let (n, e) = key[i % keylen]
    3. let c = power_mod_n(m, e, n)
    4. let s = size(n)
    5. ciphertext += encode(c, s)
10. Print ciphertext to standard output.

In the algorithm above, we encrypt the message character by character.

Each time we encrypt a character, we append the result to our ciphertext.

After all is done, we print the ciphertext to standard output.

## Decrypting an encrypted message using the private key

The algorithm for decrypting an encrypted message using the private key is described below.

1. Read the ciphertext from a file (e.g. cipher.txt) and store in a variable called ciphertext
2. Parse privatekey.txt into a list of (n, d) tuples and store in a variable called key
3. Let keylen be the length of our private key
4. Let message be the variable that stores our decrypted message
5. Let chr be a function that returns the Unicode character for a code point
6. Let size(n) be a utility function that calculates the number of bytes needed to store a positive integer n
7. Let power_mod_n(c, d, n) be a utility function that efficiently calculates c^d % n
8. Let decode(substr) be a utility function that decodes a string into a number
9. Let start be a variable that stores the starting index of a cipher
10. Let end be a variable that stores the index that is one more than the ending index of a cipher
11. Let i be the index of the current cipher in the sequence of ciphers
12. while start < lengthof(ciphertext)
    1. let (n, d) = key[i % keylen]
    2. let s = size(n)
    3. let end = start + size
    4. let substr = ciphertext[start:end]
    5. let c = decode(substr)
    6. let m = power_mod_n(c, d, n)
    7. message += chr(m)
    8. i += 1
    9. start += size
13. Print message to standard output

In the algorithm above, we decrypt the message cipher by cipher.

We can think of the ciphertext as a sequence of encoded ciphers.

We get the start index and the end index of an encoded cipher.

We decode that portion of the ciphertext (ciphertext[start:end]) into a variable called c.

The variable c stands for "cipher".

Then we calculate the code point of the decrypted character using the calculation m = power_mod_n(c, d, n).

This function efficiently calculates c^d % n.

Thus m = c^d % n.

The variable m stores the code point of the original Unicode character.

Then we use the chr function to convert the code point into its Unicode representation (i.e. the Unicode character).

We append the Unicode character (that is, chr(m)) to the message. The message variable stores our decrypted message.

We increment i, because we are going to look at the ith cipher block in our cipher text during the next iteration.

We set start to start + size, because the start variable needs to point to the beginning of the next encoded cipher.

So we process a sequence of encoded ciphers, and each time we process an encoded cipher, we decode it, and then decrypt the cipher.

We use the operation m = c^d % n to decrypt the cipher.

After we have processed each encoded cipher, we have finished processing the ciphertext, and we can print our decrypted message.

The heart of the encryption algorithm is the computation c = m^e % n.

The heart of the decryption algorithm is the computation m = c^d % n.

The modulus n is the product of two prime numbers (p and q) so it has special properties in modular arithmetic.

That's one reason why the RSA algorithm is based on prime numbers... because of their properties in modular arithmetic.

## Usage

I've waited until the end of this document to write a section on usage.

Sorry about that... I could have made it the first section.

Without further adieu, let's explain how to use the files in this repository.

    # RSA keys are based on prime numbers, so the first thing we do is generate a prime table
    % python primetable.py 1e5

    # Before we proceed, we can open the prime table and inspect the prime table
    % python
    >>> import primetable
    >>> primetable.load()
    >>> primetable.size()
    100000
    >>> primetable.table[0:10]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> primetable.get(-1)
    1299709

    # Now we can use the keytable.py program to generate RSA keys and store them in a key table
    % python keytable.py -n 10 -min 1e3 -max 1e4
    ...
    .
    .
    Generated 10 keys for tmin=1000 and tmax=10000 in 2.7593281269073486 seconds

    # The command above generates 10 RSA keys based on prime numbers between 1,000 (1e3) and 10,000 (1e4)
    # The 10 RSA keys that we generated are stored in the file keytable.pickle
    # Now we can use the keys in our key table to create a public key and a private key
    # We will use a keylength of 8
    % python keygen.py -kl 8 -min 1e3 -max 1e4
    Created key pair in publickey.txt and privatekey.txt

    # We chose 8 keys from our key table
    # Every key is based on prime numbers between 1e3 and 1e4
    # To make the algorithm more secure we can increase the minimum and maximum thresholds and we can also increase the key length
    # Our public key is a list of 8 (n, e) tuples and our private key is a list of 8 (n, d) tuples
    # Now we can use our public key to encrypt the message stored in message.txt
    % python encrypt.py message.txt
    <encrypted message>

    # Let's encrypt the message stored in message.txt and write the encrypted message to cipher.txt
    % python encrypt.py message.txt > cipher.txt

    # Let's quickly view the contents of cipher.txt to verify that it holds the encrypted message
    % cat cipher.txt
    <encrypted message>

    # We verified that cipher.txt holds the encrypted message
    # Now we are going to decrypt the contents of cipher.txt and print the result to standard output
    % python decrypt.py cipher.txt
    Hello
    My name is Andrew
    I am writing this on Saturday, June 28, 2025
    It is summer
    According to Google, the summer season began two Fridays ago
    I am currently watching The Legend of Korra on YouTube
    (I purchased the show on YouTube)
    I really like this show
    I am a big fan of Avatar: The Last Airbender and The Legend of Korra
    We finished watching Avatar earlier this year

    # There we go... we encrypted a message and saved the encrypted message in cipher.txt
    # Then we decrypted the contents of cipher.txt and printed the result to standard output
    # The result that we see in standard output is the original message, as expected
    # We just demonstrated how we can use the files in this repository to accomplish the following:
    # 1) Create a prime table of the first n primes
    # 2) Create RSA keys and store them in a key table
    # 3) Create a public key and a private key using keys from our key table
    # 4) Use the public key to encrypt a message
    # 5) Use the private key to decrypt a message
    # To be clear, the main files that we used are primetable.py, keytable.py, keygen.py, encrypt.py, and decrypt.py.
    # The other files are auxiliary files that are used by the main modules.
    # I hope that this code section explains how to use the files in this repository.
    # I thought that the easiest way to explain it would be to give an example.
    # Thanks for reading.
    # Today is Tuesday, August 5, 2025.
    # I'm a little tired today so my plan is to take it easy...
    # In my family we use the words "best decision" when we talk about decision making.
    # In my family we use the words "best move" when we talk about chess.
    # In my family we use the words "best time" when we talk about sleep theory.
    # What is the best time to go to sleep? I don't know.
    # I think about this question a lot...
    # It might be 8pm...
