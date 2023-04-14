# enkcrypt pakai private key pengirim
# decrypt pakai public key pengirim

from rsa import *
from keccak import *
from fileOperation import *
from tkinter.messagebox import showinfo


def sign_Text(filePath: str, d: int, n: int):
    signature_array = createSignature_Text(filePath, d, n)
    # change array of int to hex
    for i in range (len(signature_array)):
        signature_array[i] = int_to_hex(signature_array[i])

    signature = array_to_string(signature_array)
    # WRITE SIGNATURE DIRECTLY IN THE FILE
    addKeyInNewLine(filePath, signature)

def sign_Binary(filePath: str, d: int, n: int):
    signature_array = createSignature_BinFile(filePath, d, n)
    # change array of int to hex
    for i in range (len(signature_array)):
        signature_array[i] = int_to_hex(signature_array[i])

    signature = array_to_string(signature_array)
    # WRITE SIGNATURE IN OTHER TXT FILE WITH SAME NAME
    signature_filename = getNameFromFilepath(filePath)
    signature_filePath = './outputFile/' + signature_filename + '.txt'
    open(signature_filePath, 'w') # create file
    addKeyInNewLine(signature_filePath, signature)

def createSignature_Text(filePath: str, d: int, n: int):
    message_digest = hashKeccak_Text(filePath)
    # Convert Binarray to List of Int
    message_digest = list(message_digest)
    # encryption
    cipher_text = []
    for m in (message_digest):
        cipher = crypt(m, d, n)
        cipher_text.append(cipher)
    return cipher_text # list[int]

def createSignature_BinFile(filePath: str, d: int, n: int):
    message_digest = hashKeccak_Binary(filePath)
    
    # Convert Binarray to List of Int
    message_digest = list(message_digest)
    print(f'Message Digest : {message_digest}')
    # encryption
    cipher_text = []
    for m in (message_digest):
        cipher = crypt(m, d, n)
        cipher_text.append(cipher)

    print(f'Signature Array : {cipher_text}')
    return cipher_text # list[int]

def addKeyInNewLine(filename, text):
    if(findSignature(filename) == None):
        try:
            f_in = open(filename, 'r')
            lines = f_in.readlines()
            # Append the new paragrap at the end of the list
            lines.append('<ds>' + text + '</ds>')
            # Open the output file for writing
            f_out =  open(filename, 'w')
            # Write the modified lines to the output file
            f_out.writelines(lines)

        except:
            raise(Exception(f'Failed to add digital signature in {filename}'))
    else:
        raise(Exception(f'File {filename} sudah ditandatangani'))

def findSignature(filePath):
    signature = ''
    f = open(filePath, 'r')
    content = f.read()
    # Add Tag
    start_tag = '<ds>'
    end_tag = '</ds>'
    # Set index
    start_index = content.find(start_tag)
    end_index = content.find(end_tag)
    
    if (start_index != -1) and (end_index != -1):
        signature = content[start_index+len(start_tag):end_index].strip()
        return signature