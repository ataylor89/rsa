# readme

## Overview

Before I begin a section on usage, let's give an overview of the project.

File | Description
---- | -----------
primetable.py | Creates a prime table of the first n primes and writes it to database/primetable.pickle
keytable.py | Maintains a key table in database/keytable.pickle and adds keys to the key table on demand
keygen.py | Creates an RSA key using the key table and the prime table
parser.py | Parses an RSA key, like the one in keys/defaultkey.txt, and returns a list of (n, e, d) tuples
util.py | Contains many useful functions, like power_mod_n, which are used in encryption and decryption
exceptions.py | Defines different exceptions that can be raised by the code in this package
primecheck.py | Contains an algorithm for determining whether a number is prime, which is useful in some of the unit tests
settings.py | Contains many settings, like the project root directory and the default key path
encrypt.py | Encrypts a message using the public key
decrypt.py | Decrypts an encrypted messsage using the private key

## Usage

To generate a primetable of 10,000 primes, we can use the following commands:

    % cd ~/Github/rsa/src
    % python primetable.py 1e4

The primetable that we generated should be written to ~/Github/rsa/database/primetable.pickle.

If the existing primetable is already sufficient, then the file is not overwritten, and the program does not proceed with the prime table generation.

To generate a keytable and add 64 keys to the keytable, we can use the following commands:

    % cd ~/Github/rsa/src
    % python keytable.py 64

This command uses the default values for tmin and tmax (1056 and 10,000).

The reason why 1056 is the default value is that the modulus (n-value) has to exceed the size of the Unicode code space, which is 0x110000 in hex or 1,114,112 in decimal. Note that 1056^2 = 1,115,136, which exceeds the size of the Unicode code space.

In other words, the codepoint for each Unicode character should be less than the modulus (that is, the n value).

Keep in mind that a public key is a series of (n, e) tuples, and a private key is a series of (n, d) tuples.

To generate an RSA key consisting of 64 (n, e, d) tuples, we can use the following commands:

    % cd ~/Github/rsa/src
    % python keygen.py 64

Once again, 1056 is the default value for tmin, because we want the n-value of each (n, e, d) tuple to exceed 0x110000.

The abbreviation tmin stands for minimum prime threshold. The primes p and q which are chosen for the key must meet or exceed tmin.

The keygen program has a default path for the generated key. The default path, for me, is ~/Github/rsa/keys/generated-key.txt.

Now, we can use our generated key to encrypt and decrypt messages.

To encrypt a message using the generated key, we can use the following commands:

    % cd ~/Github/rsa/src
    % python encrypt.py -k ~/Github/rsa/keys/generated-key.txt "hello world" -o cipher.txt

This writes the encrypted message to the file ~/Github/rsa/src/cipher.txt.

To decrypt the encrypted message, using our generated key, we can use the following commands:

    % cd ~/Github/rsa/src
    % python decrypt.py -k ~/Github/rsa/keys/generated-key.txt -i cipher.txt

It should output "hello world".

I just tested it myself... and it worked.

Now, one last thing before I wrap up this section.

It takes a long time to type a key path like ~/Github/rsa/keys/generated-key.txt.

We can actually save time by using the default key file.

Let's try encrypting a message using the default key file.

    % cd ~/Github/rsa/src
    % python encrypt.py "hello world, it's january 28, 2026" -o cipher2.txt

Now we can decrypt the encrypted message using the default key file.

    % cd ~/Github/rsa/src
    % python decrypt.py -i cipher2.txt

I just tried it, and it works. It prints "hello world, it's january 28, 2026" to standard output.

(In case you're wondering, the path to the default key file is actually a setting configured in settings.py.)

I wanted to show this alternative, because it saves time.

To summarize, we have given instructions on how to generate a primetable using primetable.py, how to maintain a keytable using keytable.py, how to generate a key file using keygen.py, how to encrypt a message using encrypt.py, and how to decrypt a message using decrypt.py.

I might add more to this readme later. But I think this section is finished.
