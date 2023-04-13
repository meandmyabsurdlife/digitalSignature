import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from signing import *
from rsa import *
from keccak import *
from fileOperation import *
from main import *


public_key = 3
private_key = 851
n = 1357

# OTHER FILE
filename = 'test/gojo.jpg'
sign_Binary(filename, private_key, n)

'''
# TXT FILE
filename1 = 'test/test_DS.txt'
sign_Text(filename1, private_key, n)
'''



