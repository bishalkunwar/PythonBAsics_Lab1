from string import printable
from random import shuffle

keys = list(printable)
shuffle_keys = list(printable)
shuffle(shuffle_keys)

maps = dict(zip(keys, shuffle_keys))
reverse_map = dict(zip(shuffle_keys, keys))

def encrypt(message):
    cipher = []
    for char in message:
        cipher_char = maps[char]
        cipher.append(cipher_char)
    return ''.join(cipher)


def decrypt(cipher):
    plain = []
    for cipher_char in cipher:
        plain_char = reverse_map[cipher_char]
        plain.append(plain_char)
    return ''.join(plain)

message = 'hello'
# Call the encrypt function

cipher = encrypt(message)
print(cipher)

# Decryption
# Call decrypt function
plain_message =  decrypt(cipher) # This print the original messaage.
print(plain_message)

