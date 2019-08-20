# coding: utf-8
from pwn import *
from Crypto.Cipher import AES
import itertools
from tqdm import tqdm
import string
import hashlib
import teddy
import re

def red(prt):
    return "\033[91m{}\033[00m".format(prt)
def grn(prt):
    return "\033[92m{}\033[00m".format(prt)
def cyn(prt):
    return "\033[96m{}\033[00m".format(prt)
def flag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('UDCTF', cyn('UDCTF')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))

### TEST HACK IV ###
print '\nTESTING...\n'
k = 'as'
key = 'upersecretkey!'
iv = '2fcb848b15ebf54c21b1fe8cc76a1f75'.decode('hex')
pt = 'abcdefghijklmnop1234567891234567'
pt1 = pt[:16]
pt2 = pt[16:]

cipher = AES.new(k+key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pt)
ct1 = ct[:16]
ct2 = ct[16:]

print 'iv  =', iv.encode('hex')
print 'key =', k+key
print 'ct1 =', ct1.encode('hex'), '|', 'ct2 =', ct2.encode('hex')
print 'pt1 =', pt1.encode('hex'), '|', 'pt2 =', pt2.encode('hex')
print 'plaintext =', pt

cipher = AES.new(k+key)
ct1 = xor(cipher.decrypt(ct2), pt2)
iv  = xor(cipher.decrypt(ct1), pt1)
print 'hacked ct1 =', ct1.encode('hex')
print 'hacked iv  =', iv.encode('hex')

### PWN HACK IV ###
print '\nHACKING...\n'
k = '2Hup4mHRqGt9bD'
pt = 'Encrypt this with AES for me plz'
pt1 = pt[:16]
pt2 = pt[16:]
ct2 = '47d07e086873f69a09714c6da3f89252'.decode('hex')
ct1 = 'baAAAAAAAAAAAAAAAAAAAAAAAAAAcbf6'.decode('hex')

print 'iv  =', 'UNKNOWN...'
print 'key =', '??'+k
print 'ct1 =', ct1.encode('hex'), ' | ', 'ct2 =', ct2.encode('hex').replace('A','?')
print 'pt1 =', pt1.encode('hex'), ' | ', 'pt2 =', pt2.encode('hex')
print 'plaintext =', pt

print '#'*80
print 'HACKING KEY...'
chars = [chr(i) for i in range(256)]
total = teddy.get_length_itertools('product', chars, 2)

keys = {}
for cc in tqdm(itertools.product(chars, repeat=2), desc='Generating Keys', position=0, total=total):
    c = ''.join(cc)
    cipher = AES.new(c+k)
    # get ct1 from decrypt(ct2) ^ pt2
    test_ct1 = xor(cipher.decrypt(ct2), pt2)
    if test_ct1[0] == ct1[0] and test_ct1[14:16] == ct1[14:16]:
        key = c + k
        ct1 = test_ct1
        keys[key] = ct1
        print '\npossible key:', key, '\n', 'hacked_ct1 =', test_ct1.encode('hex'), '\n'
        
print '#'*80, '\n'
print 'Number of possible keys found:', len(keys)
print '#'*80

### VERIFYING ###
print '\nHACKING IV..\n'
iv_s = {}
for key, ct1 in keys.items():
    cipher = AES.new(key)
    iv = xor(cipher.decrypt(ct1), pt1)
    iv_s[key] = {}
    iv_s[key][iv]  = iv
    iv_s[key][ct1] = ct1
    iv_s[key][ct2] = ct2
    print '\nhacked iv =', iv.encode('hex'), iv

print '#'*80
print '\nVERIFYING DATA...\n'
k_   = '??2Hup4mHRqGt9bD'
iv_  = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
pt   = 'Encrypt this with AES for me plz'
pt_1 = pt[:16]
pt_2 = pt[16:]
ct_2 = '47d07e086873f69a09714c6da3f89252'.decode('hex')
ct_1 = 'baAAAAAAAAAAAAAAAAAAAAAAAAAAcbf6'.decode('hex')

for key, obj in iv_s.items():
    iv  = iv_s[key][iv]
    ct1 = iv_s[key][ct1]
    ct2 = iv_s[key][ct2]

    print '#'*80
    print 'originial values...'
    print 'iv   =', iv_
    print 'key  =', k_
    print 'ct_1 =', ct_1.encode('hex'), ' | ', 'ct_2 =', ct_2.encode('hex')
    print 'pt_1 =', pt_1.encode('hex'), ' | ', 'pt_2 =', pt_2.encode('hex')
    print 'plaintext =', pt
    print '#'*80
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pt)
    ct1_ = ct[:16]
    ct2_ = ct[16:]

    print '#'*80
    print 'hacked values...'
    print 'iv   =', iv
    print 'key  =', key
    print 'ct1_ =', ct1_.encode('hex'), ' | ', 'ct2_ =', ct2_.encode('hex')
    print 'pt_1 =', pt_1.encode('hex'), ' | ', 'pt_2 =', pt_2.encode('hex')
    print 'plaintext =', pt
    print '#'*80

    if ct_1[0] == ct1_[0] and ct_1[14:16] == ct1_[14:16] and ct2_ == ct_2:
        print '\nsuccess ...'
        temp = '\tUDCTF{' + iv + '}'
        break

print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
