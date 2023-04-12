import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from keccak import *
from fileOperation import *

def testKeccak_text(filename):
    hash_string = hashKeccak_Text(filename)

    print(f'Hasil hash SHA-3 dari ({filename}) :')
    print(hash_string)
    print(f'Array hash SHA-3 dari ({filename}) :')
    print(list(hash_string))

def testKeccak_binary(filename):
    hash_string = hashKeccak_Binary(filename)

    print(f'Hasil hash SHA-3 dari file ({filename}) :')
    print(hash_string)
    print(f'Array hash SHA-3 dari file ({filename}) :')
    print(list(hash_string))

testKeccak_text('D:\\SEM6\\Kriptografi dan Koding\\Code\\Tucil 3\\test\\test.txt')
print()
testKeccak_binary("D:\Picture\gojo.jpg")
