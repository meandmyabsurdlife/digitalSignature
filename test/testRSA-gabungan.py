import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from rsa import *
from fileOperation import *

x = '100120089876'

'''
 input enkripsi dan dekripsi merupakan message digest dengan tipe bytes
'''
message_digest = [72, 69, 76, 76, 79, 44, 32, 87, 79, 82, 76, 68, 33]
def testing_RSA(p: int, q: int, message_digest: list[int]):
    # change to array of int

    print('Input :')
    print(message_digest)
    loop = True
    #while (loop == True):

    # GENERATE KEY
    if (isPrima(p)==True and isPrima(q)==True): 
        n = calculate_n(p,q)

        totion_n = calculate_totion_n(p,q)

        print(f'nilai possible untuk e, dengan totion-n = {totion_n} :')
        array_e = generatePossiblePublicKey(totion_n)
        print(array_e)  
        e = int(input('Masukkan nilai e: '))
        
        while (e not in (array_e)):
            print(f'{e} tidak relatif prima dengan {totion_n}')
            e = int(input('Masukkan nilai e: '))

        print('\n-----INFORMASI KUNCI-----')
        print(f"Nilai n : {n}")
        print(f"Nilai totion-n : {n}")
        print(f"Kunci publik : {e}")
        '''
        if (e not in (array_e)):
           print(f'{e} tidak relatif prima dengan {totion_n}')
        print(f"Kunci public : {e}")
        '''

        d = generatePrivateKey(e, totion_n)
        print(f"Kunci privat : {d}")  
    else:
        print('p atau q BUKAN prima')   

    # ENCRYPT
    print('\n-----ENKRIPSI-----')
    cipher_text = []
    for char in (message_digest):
        cipher = crypt(char, d, n)
        cipher_text.append(cipher)
    print(f'array of int enkripsi : {cipher_text}')

    for i in range (len(cipher_text)):
        cipher_text[i] = int_to_hex(cipher_text[i]) # change to hex
    print(f'array of hex enkripsi : {cipher_text}')

    print(f'\nsignature : {array_to_string(cipher_text)}')

    # DECRYPT
    print('\n-----DEKRIPSI-----')
    print(f'input dekripsi : {cipher_text}')
    plain_text = []
    for i in range (len(cipher_text)):
        cipher_text[i] = hex_to_int(cipher_text[i]) # change to int
        plain = crypt(cipher_text[i], e, n)
        plain_text.append(plain) 
    print(f'array plain text : {plain_text}')
    print(f'array input awal : {message_digest}')

    #print(f'\string dari array plain text : {array_to_string(plain_text)}')


    if (message_digest == plain_text):
        print('\nmessage digest = plain text, SUDAH BENAR')
    else:
        print('\nmessage digest ≠ plain text, SALAH')


testing_RSA(23, 59, message_digest)