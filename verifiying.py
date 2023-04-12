import rsa
import signing

def isValidPrivateandPublic(e, d, n_private, n_public):
    if (n_private == n_public):
        return True
    else:
        return False


def verify(message: str, signature: str, e, d, n_private, n_public): # str, 
    # Melakukan pengecekan MD' dan MD
    # MD' : message_digest
    # MD : decrypt_signature

    message_digest = signing.hash(message) # array of int

    # change decimal signature to group by four
    decrypt_signature = [] # array of int
    for m in (signature):
        plain = rsa.crypt(m, e, n)
        decrypt_signature.append(plain)

    if (message_digest == decrypt_signature):
        return True
    else:
        return False
    

