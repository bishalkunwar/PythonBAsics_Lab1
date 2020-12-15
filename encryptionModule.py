#encryption module api using caser and mono encryption.

from string import printable as letters
from random import shuffle

keys = list(printable)
shuffle_keys = list(printable)
shuffle(shuffle_keys)

maps = dict(zip(keys, shuffle_keys))
reverse_map = dict(zip(shuffle_keys, keys))

def caser_encrypt(message, key):
    cipher = []
    for a in message:
        position = letters.find(a)
        newPosition = position + key %len(letters)
        encrypt = letters[newPosition]
        cipher.append(encrypt)

    return ''.join(cipher)

def caser_decrypt (cipher, key):
    plainText = []
    for a in cipher:
        position = letters.find(a)
        newPosition = position - key %len(letters)
        decrypt = letters[newPosition]
        plainText.append(plainText)

    return ''.join(plainText)

def mono_encrypt(message):
    cipher = []
    for char in message:
        cipher_char = maps[char]
        cipher.append(cipher_char)
    return ''.join(cipher)


def mono_decrypt(cipher):
    plain = []
    for cipher_char in cipher:
        plain_char = reverse_map[cipher_char]
        plain.append(plain_char)
    return ''.join(plain)

message = 'hello'
# Call the encrypt function

cipher = caser_encrypt(message,3)
print(cipher)
cipher = mono_encrypt(message)
print(cipher)

# Decryption
# Call decrypt function
plain_message = caser_decrypt(cipher,3)
print(plain_message)
plain_message = mono_decrypt(cipher) # This print the original messaage.
print(plain_message)