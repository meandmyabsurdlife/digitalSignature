import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from signing import *
from rsa import *
from keccak import *
from fileOperation import *

def addKeyInNewLine(filename, text):
    try:
        f_in = open(filename, 'r')
        lines = f_in.readlines()
        # Add a new line
        lines.append('\n')
        # Append the new paragraph as a new string to the end of the list
        lines.append('<ds>\n' + text + '\n</ds>')

        # Open the output file for writing
        f_out =  open(filename, 'w')
        # Write the modified lines to the output file
        f_out.writelines(lines)
    except:
        raise(Exception(f'Failed to add digital signature in {filename}'))


public_key = 3
private_key = 851
n = 1357

print('\n--------SIGNING TEXT (*.txt)--------')
filename1 = 'test\\test.txt'
signature = sign_Text(filename1, private_key, n)
print(signature)
# ADD DIGITAL SIGNATURE
addKeyInNewLine(filename1, signature)

print('\n--------SIGNING FILE--------')
