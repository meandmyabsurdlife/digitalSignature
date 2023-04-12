import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from rsa import *
from fileOperation import *

def test_intToBigNum(number):
    print(int_to_BigNumber(number))

def test_isPrima(number):
    print(f'prima {number} : {isPrima(number)}')

def test_isPrimaRelative(number1, number2):
    print(f'prima relatif{number1, number2} : {isPrimaRelative(number1, number2)}')

def test_calculateN(number1, number2):
    print(f'nilai n dari {number1, number2} : {calculate_n(number1, number2)}')

def test_calculateTotionN(number1, number2):
    print(f'nilai totion-n dari {number1, number2} : {calculate_totion_n(number1, number2)}')

def test_generatePossiblePublicKey(number):
    print(f'nilai public key yg mungkin dari totion-n = {number} : {generatePossiblePublicKey(number)}')

def test_generatePrivateKey(number1, number2):
    print(f'nilai private key dari {number1, number2} : {generatePrivateKey(number1, number2)}')

def test_crypt(number, key, n):
    print(f'nilai crypt dari {number, key, n} : {crypt(number, key, n)}')

def test_intToHex(number):
    print(f'nilai hex dari {number} : {int_to_hex(number)}')

def test_hexToInt(hexString):
    print(f'nilai int dari {hexString} : {hex_to_int(hexString)}')

def test_strToArrayAscii(string):
    print(f'Array ASCII dari {string} : {str_to_arrayAscii(string)}')

def test_arrayToString(array):
    print(f'string dari {array} : {array_to_string(array)}')




# TESTING
test_intToBigNum(3567890121908394785747584982943190130193043787857487845847929181)
test_isPrima(23)
test_isPrimaRelative(int_to_BigNumber(23), int_to_BigNumber(59))
test_calculateN(int_to_BigNumber(23), int_to_BigNumber(59))
# test_calculateN(int_to_BigNumber(10), int_to_BigNumber(5))

test_calculateTotionN(int_to_BigNumber(23), int_to_BigNumber(59))

totion_n = calculate_totion_n(int_to_BigNumber(23), int_to_BigNumber(59))

# GENERATE PUBLIC KEY       
test_generatePossiblePublicKey(totion_n)
test_generatePossiblePublicKey(1276)
test_generatePossiblePublicKey(1357)

# GENERATE PRIVATE KEY   
public_key = int(input('Masukkan nilai e :'))
test_generatePrivateKey(public_key, totion_n)

# CRYPT
test_crypt(100000098, generatePrivateKey(public_key, totion_n), calculate_n(int_to_BigNumber(23), int_to_BigNumber(59)))

# INT-HEX
test_intToHex(100000098)
test_hexToInt('0x5f5e162')

test_strToArrayAscii('HELLO, WORLD!')
test_arrayToString(['a', 6, 7, 8])
