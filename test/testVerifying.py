import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from verifiying import *

public_key = 3
private_key = 851
n = 1357
n_private = n
n_public = n


filePath1 = 'test/test_DS.txt'
print(verify_text(filePath1, public_key, n_private, n_public))


filePath2 = 'test/gojo.jpg'
signaturePath = 'outputFile/gojo.txt'
print(verify_BinFile(filePath2, signaturePath, public_key, private_key, n_private, n_public))

'''
print("-----MESAGE DIGEST'-----")
message = readMessage_text('test/test_DS.txt')
print(message)
md = list(hashKeccak_message(message))
print(md)


print('-----DIGITAL SIGNATURE-----')
ds = findSignature('test/test_DS.txt')
ds = signature_to_listofInt(ds)

print(ds)
print('-----DECRYPT DIGITAL SIGNATURE-----')
for i in range(len(ds)):
    ds[i] = crypt(ds[i], public_key, n)
print(ds)

print(ds == md)
'''