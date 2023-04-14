import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from verifiying import *

def read_key(filename):
    # Change label contents
    content = readFile(filename)

    content = content.strip('()').split(',')
    
    key = int(content[0])
    n = int(content[1])
    return [key, n]

pub_key = read_key("D:\\uji\\kunci\\pub1.pub")
print('public_key')
print(pub_key)
public_key = pub_key[0]
n_public = pub_key[1]

pri_key = read_key("D:\\uji\\kunci\\pri1.pri")
print('private_key')
print(pri_key)
private_key = pri_key[0]
n_private = pri_key[1]


filePath1 = 'D:/uji/file/test3.txt'
print(verify_text(filePath1, public_key, n_private, n_public))

'''
filePath2 = 'test/gojo.jpg'
signaturePath = 'outputFile/gojo.txt'
print(verify_BinFile(filePath2, signaturePath, public_key, private_key, n_private, n_public))


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