import hashlib
from fileOperation import readFile
from fileOperation import readBinaryFile

def hashKeccak_Text(filename) -> bytes: # str -> bytes
    # read file
    message = readFile(filename)
    return(hashKeccak_message(message))


def hashKeccak_message(message):
    # change str to bytes
    message_bytes = message.encode('iso-8859-1')
    sha3_256 = hashlib.sha3_256()

    # hash the message bytes
    sha3_256.update(message_bytes)

    digest_bytes = sha3_256.digest()

    return digest_bytes

def hashKeccak_Binary(filename) -> bytes:
    # read Binary
    bin = readBinaryFile(filename)
    sha3_256 = hashlib.sha3_256()

    # hash the message bytes
    sha3_256.update(bin)

    digest_bytes = sha3_256.digest()

    return digest_bytes
