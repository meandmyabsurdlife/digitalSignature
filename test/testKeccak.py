import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)
print(sys.path)

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

testKeccak_text('test\\test.txt')
print()
testKeccak_binary("test\\\gojo.jpg")