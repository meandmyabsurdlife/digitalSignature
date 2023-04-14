import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from signing import *
from rsa import *
from keccak import *
from fileOperation import *

from verifiying import *

'''
public_key = 3
private_key = 851
n = 1357
'''

'''
# OTHER FILE
filename = 'test/gojo.jpg'
sign_Binary(filename, private_key, n)

'''
# TXT FILE
def read_key(filename):
    # Change label contents
    content = readFile(filename)

    content = content.strip('()').split(',')
    
    key = int(content[0])
    n = int(content[1])
    return [key, n]

pub_key = read_key("D:\\uji\\kunci\\pub1.pub")
print('public_key : ')
print(pub_key)
public_key = pub_key[0]
n_public = pub_key[1]

pri_key = read_key("D:\\uji\\kunci\\pri1.pri")
print('private_key :')
print(pri_key)
private_key = pri_key[0]
n_private = pri_key[1]

filePath1 = "D:/uji/file/test2.txt"

#sign_Text(filePath1, private_key, n_public)
print(verify_text(filePath1, public_key, n_private, n_public))






