# enkcrypt pakai private key pengirim
# decrypt pakai public key pengirim

from rsa import *
from keccak import *

'''
def hash(message: str) -> list[int]: # str -> array of int
    message_digest = hashKeccak_Text(message)
    return list(message_digest)
'''
def sign_Text(message: str, d: int, n: int) -> str: # str, int, int -> str

    message_digest = hashKeccak_Text(message)
    # Convert Binarray to List of Int
    message_digest = list(message_digest)

    # encryption
    cipher_text = []
    for m in (message_digest):
        cipher = crypt(m, d, n)
        cipher_text.append(cipher)
    # change array of int to hex
    for i in range (len(cipher_text)):
        cipher_text[i] = int_to_hex(cipher_text[i])

    signature = array_to_string(cipher_text)
    return signature

def sign_Binary(filePath, d, n):

    message_digest = hashKeccak_Binary(filePath)
    # Convert Binarray to List of Int
    message_digest = list(message_digest)

    # encryption
    cipher_text = []
    for m in (message_digest):
        cipher = crypt(m, d, n)
        cipher_text.append(cipher)
    # change array of int to hex
    for i in range (len(cipher_text)):
        cipher_text[i] = int_to_hex(cipher_text[i])
    
    signature = array_to_string(cipher_text)
    return signature
