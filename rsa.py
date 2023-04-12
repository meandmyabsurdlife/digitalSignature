import gmpy2
import math
import sympy
from Crypto.Util import number

# https://rsa-calculator.netlify.app/

# d : private key
# e : public key


# RSA KEY GENERATOR
def int_to_BigNumber(number: int): # -> mpz
    # Mengubah data int menjadi object Big Number
    return gmpy2.mpz(number)

def isPrima(a: int) -> bool:# int  -> Boolean
    # Memeriksa apakah suatu bilangan adalah bilangan prima
    return (sympy.isprime(a))
    '''
    found = False
    if(a > 1):
        # check factors
        for i in range(2, ((a//2) + 1)):
            if (a%i == 0):
                found = True
        # check found
        if (found == True):
            return False
        else:
            return True
    else:
        return False 
    '''      

def isPrimaRelative(a: int, b) -> bool: # -> boolean
    # Memeriksa apakah dua bilangan relatif prima
    fpb = math.gcd(a,b)
    if (fpb == 1):
        return True
    else:
        return False

def calculate_n(p, q): # -> int
    # Menghitung nilai n = p * q
    if (isPrima(p) and isPrima(q)): # taruh di UI ?
        return p*q
    else:
        print(f'{p} atau {q} bukan prima')

def calculate_totion_n(p, q): # -> int
    # Menghitung nilai totion n = (p - 1)*(q - 1)
    if (isPrima(p) and isPrima(q)): # taruh di UI ?
        return (p-1)*(q-1)
    else:
        print(f'{p} atau {q} bukan prima')

def generatePossiblePublicKey(totion_n: int) -> list[int]:# -> array of int
    # generate nilai e yang relatif prima terhadap totion n
    # e < n
    possible_e = []

    for i in range (2, totion_n): # bilangan prima mulai dari 2
        if (isPrimaRelative(i, totion_n)):
            possible_e.append(i)
    return possible_e

def generatePrivateKey(e: int, totion_n: int) -> int: # -> int
    # Mengitung nilai d 
    # dengan rumus d = (1 + (k * (totion n)))/e
    # dengan k : {1,2,...}
    # hasil d adalah int

    k = 1
    loop = True
    while (loop == True):
        phi = 1 + (k * totion_n)
        if ((phi % e) == 0):  # e faktor dari (1 + (k * (totion n)))
            d = phi/e
            loop = False
        else: 
            k = k + 1

    return int(d)

# ENCRYPT & DECRYPT
def crypt(decimal: int, key: int, n: int) -> int: # int, int, int -> int
    # change int to bignumber
    big_decimal = int_to_BigNumber(decimal)
    big_key = int_to_BigNumber(key)
    big_n = int_to_BigNumber(n)

    cipher_text = (big_decimal**big_key)%big_n
    return cipher_text

# DATA PROCESSING FUNCTION
def int_to_hex(number: int) -> hex: # int -> hex
    return hex(number)

def hex_to_int(hexadecimal: hex) -> int: # hex -> int
    return int(hexadecimal, 0)

def str_to_arrayAscii(string: str) -> list[int]: # str -> array of int
    # Mengubah string ke karakter ascii
    ascii_array = []
    for i in range (len(string)):
        asciiText = ord(string[i])
        ascii_array.append(asciiText)
    return ascii_array

def array_to_string(array) -> str: #  array 
    string = ''
    for i in range (len(array)):
        string += str(array[i]) 

    return string

'''
def group_in_four(text: str) -> list[int]: # str -> array of int
    # '12345678' -> [[1234], [5678]]
    group_four_array = []
    for i in range(0, len(text), 4):
        group_for_string = "".join(text[i:i + 4])
        group_four_array.append(int(group_for_string))

    return group_four_array

def block_in_four(text: str) -> list[int]: # str -> array of int
    # 'abcdefgh' -> [['ab']['cd']['ef']['gh']]
    group_four_array = []
    for i in range(0, len(text), 2):
        two_char = "".join(text[i:i + 2])
        group_four_array.append(two_char)

    for i in range(len(group_four_array)):
        for j in range(len(i)):
            pass

    return group_four_array

'''

'''
def decrypt(decimal, d, n): # int, int, int -> hex
    # change int to bignumber
    big_decimal = int_to_BigNumber(decimal)
    big_d = int_to_BigNumber(d)
    big_n = int_to_BigNumber(n)

    message = (big_decimal**big_d)%big_n
    return message
'''
# encrypt, decrypt algoritmanya samaa, cuman parameter yg beda
# yg satu e, yg satu d

'''
def encrypt(hexadecimal, e, n): # array of hex, int, int -> hex
    decimal = hex_to_int(hexadecimal)

    # change int to bignumber
    big_decimal = int_to_BigNumber(decimal)
    big_e = int_to_BigNumber(e)
    big_n = int_to_BigNumber(n)

    cipher_text = (big_decimal**big_e)%big_n
    return cipher_text

def decrypt(hexadecimal, d, n): # hex, int, int -> hex
    decimal = hex_to_int(hexadecimal)

    # change int to bignumber
    big_decimal = int_to_BigNumber(decimal)
    big_d = int_to_BigNumber(d)
    big_n = int_to_BigNumber(n)

    message = (big_decimal**big_d)%big_n
    return message
'''