import gmpy2
import math
import sympy

# https://rsa-calculator.netlify.app/

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
    return p*q

def calculate_totion_n(p, q): # -> int
    # Menghitung nilai totion n = (p - 1)*(q - 1)
    return (p-1)*(q-1)

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
    '''
    k = 1
    loop = True
    while (loop == True):
        phi = 1 + (k * totion_n)
        if ((phi % e) == 0 and (phi/e != e)):  # e faktor dari (1 + (k * (totion n)))
            d = phi/e
            loop = False
        else: 
            k = k + 1
    '''
    d = (pow(e, -1, totion_n))

    return int(d)

# ENCRYPT & DECRYPT
def crypt(decimal: int, key: int, n: int) -> int: # int, int, int -> int
    # change int to bignumber
    big_decimal = int_to_BigNumber(decimal)
    big_key = int_to_BigNumber(key)
    big_n = int_to_BigNumber(n)

    cipher_text = ((big_decimal**big_key)%big_n)
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