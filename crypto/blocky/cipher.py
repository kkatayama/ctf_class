from Crypto.Cipher import DES
import string
import os

def super_encryption(plaintext, key):
    ct = ""
    cipher = DES.new(key)
    for a_letter in plaintext:
        ct += cipher.encrypt(a_letter*8)
    return ct

with open('flag', 'r') as f:
    flag = f.read().strip()

key = os.urandom(8)
ct1 = super_encryption(string.printable, key)
ct2 = super_encryption(flag, key)

with open('ct1','w') as f:
    f.write(ct1.encode('hex'))

with open('ct2','w') as f:
    f.write(ct2.encode('hex'))
