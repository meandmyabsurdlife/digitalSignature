from rsa import *
from signing import *

def isValidPrivateandPublic(n_private, n_public):
    '''
    check if n_private key = n_public_key
    '''
    if (n_private == n_public):
        return True
    else:
        return False
    
def readMessage_text(filePath):
    '''
    Read contents before <\ds> tag from *.txt file
    '''
    with open(filePath, 'r') as f:
        # Read the entire file contents into a string
        contents = f.read()
        # Find the index of the first occurrence of '<ds>'
        end_tag = contents.find('<ds>')
        # Extract the content before the '<ds>' tag
        message = contents[:end_tag]
        return message

def signature_to_listofInt(string_hex: str):
    # Pisahkan string berdasarkan "0x"
    hex_list = string_hex.split("0x")[1:]
    '''
    # Hapus prefix "0x"
    hex_list = [hex_str.lstrip("0") or "0" for hex_str in hex_list]
    '''
    # split into array of hex
    hex_list = ['0x' + hex_str for hex_str in hex_list]
    # change to int
    hex_list = [int(hex_str, 0) for hex_str in hex_list]

    return hex_list

def verify_text(filePath: str, public_key: int, n_private: int, n_public: int) -> bool:
    # Melakukan pengecekan MD' dan MD
    # MD' : message_digest
    # MD : decrypt_signature
    message = readMessage_text(filePath)
    #print(f'Message : {message}')
    #print(len(message))

    if (isValidPrivateandPublic(n_private,n_public)):
        # Calculate MD
        message_digest = list(hashKeccak_message(message))
        #print(f'Message digest : {message_digest}')
        #print(len(message_digest))

        # Calculate MD'
        ds = findSignature(filePath)
        ds = signature_to_listofInt(ds)
        #print(f'Signature sebelum decrypt : {ds}')
        #print(len(ds))
        # DECRYPT DIGITAL SIGNATURE
        for i in range(len(ds)):
            ds[i] = crypt(ds[i], public_key, n_public)
        #print(f'Signature sesudah decrypt : {ds}')
        #print(len(ds))

        return message_digest == ds
    else:
        raise(Exception('Kunci Publik dan Kunci Private tidak berpadanan'))


def verify_BinFile(filePath: str, signaturePath: str, public_key: int, private_key: int, n_private: int, n_public: int) -> bool:
    if (isValidPrivateandPublic(n_private,n_public) == True):
        # Calculate MD
        message_digest = list(hashKeccak_Binary(filePath))

        # Calculate MD'
        ds = findSignature(signaturePath)
        ds = signature_to_listofInt(ds)
        # DECRYPT DIGITAL SIGNATURE
        for i in range(len(ds)):
            ds[i] = crypt(ds[i], public_key, n_public)

        return message_digest == ds
    else:
        raise(Exception('Kunci Publik dan Kunci Private tidak berpadanan'))
