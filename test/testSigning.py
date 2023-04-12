import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from signing import *
from fileOperation import *

print('\n--------SIGNING TEXT (*.txt)--------')
filename1 = 'D:\\SEM6\\Kriptografi dan Koding\\Code\\Tucil 3\\test\\test.txt'

public_key = 3
private_key = 851
n = 1357

signature = sign_Text(filename1, private_key, n)
print(signature)

# ADD DIGITAL SIGNATURE
