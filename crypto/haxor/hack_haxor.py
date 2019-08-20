# coding: utf-8
# %load hack_haxor.py
from Crypto.Util.number import *
from pwn import *
from hashlib import md5
from binascii import hexlify, unhexlify
from tqdm import tqdm
import itertools
import string
import re

def red(prt):
    return "\033[91m{}\033[00m".format(prt)
def grn(prt):
    return "\033[92m{}\033[00m".format(prt)
def cyn(prt):
    return "\033[96m{}\033[00m".format(prt)
def sflag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('UDCTF', cyn('UDCTF')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))

# from secret import key, flag
BLOCK_LENGTH = 16
KEY_LENGTH = 3
ROUND_COUNT = 16

sbox = [210, 213, 115, 178, 122, 4, 94, 164, 199, 230, 237, 248, 54,
        217, 156, 202, 212, 177, 132, 36, 245, 31, 163, 49, 68, 107,
        91, 251, 134, 242, 59, 46, 37, 124, 185, 25, 41, 184, 221,
        63, 10, 42, 28, 104, 56, 155, 43, 250, 161, 22, 92, 81,
        201, 229, 183, 214, 208, 66, 128, 162, 172, 147, 1, 74, 15,
        151, 227, 247, 114, 47, 53, 203, 170, 228, 226, 239, 44, 119,
        123, 67, 11, 175, 240, 13, 52, 255, 143, 88, 219, 188, 99,
        82, 158, 14, 241, 78, 33, 108, 198, 85, 72, 192, 236, 129,
        131, 220, 96, 71, 98, 75, 127, 3, 120, 243, 109, 23, 48,
        97, 234, 187, 244, 12, 139, 18, 101, 126, 38, 216, 90, 125,
        106, 24, 235, 207, 186, 190, 84, 171, 113, 232, 2, 105, 200,
        70, 137, 152, 165, 19, 166, 154, 112, 142, 180, 167, 57, 153,
        174, 8, 146, 194, 26, 150, 206, 141, 39, 60, 102, 9, 65,
        176, 79, 61, 62, 110, 111, 30, 218, 197, 140, 168, 196, 83,
        223, 144, 55, 58, 157, 173, 133, 191, 145, 27, 103, 40, 246,
        169, 73, 179, 160, 253, 225, 51, 32, 224, 29, 34, 77, 117,
        100, 233, 181, 76, 21, 5, 149, 204, 182, 138, 211, 16, 231,
        0, 238, 254, 252, 6, 195, 89, 69, 136, 87, 209, 118, 222,
        20, 249, 64, 130, 35, 86, 116, 193, 7, 121, 135, 189, 215,
        50, 148, 159, 93, 80, 45, 17, 205, 95]
p = [3, 9, 0, 1, 8, 7, 15, 2, 5, 6, 13, 10, 4, 12, 11, 14]


def xor2(a, b):
    return bytearray(map(lambda s: s[0] ^ s[1], zip(a, b)))


def cipher(key, pt):
    assert len(pt) == BLOCK_LENGTH
    assert len(key) == KEY_LENGTH
    key = bytearray(unhexlify(md5(key).hexdigest()))
    ct = bytearray(pt)
    for _ in range(ROUND_COUNT):
        ct = xor2(ct, key)
        for i in range(BLOCK_LENGTH):
            ct[i] = sbox[ct[i]]
        nct = bytearray(BLOCK_LENGTH)
        for i in range(BLOCK_LENGTH):
            nct[i] = ct[p[i]]
        ct = nct
    return hexlify(ct)

# key = '000'
# flag = '00000000'
# print("Encrypting permutations yo!: %s" % cipher(key, b"permutations yo!"))
# print("Encrypted flag: %s" % cipher(key, flag))
#Output
#Encrypting permutations yo!: 34e78a7b71641230f76bbdb6081a2a87
#Encrypted flag: dac6cc1689dd6b3e516ae082d9430510
chars = ''.join([chr(c) for c in range(0, 256)])
'''
keys = [''.join(c) for c in itertools.product(chars, repeat=3)]
for key in tqdm(keys):
    key = ''.join(key)
    ct = cipher(key, b"permutations yo!")
    if ct == "34e78a7b71641230f76bbdb6081a2a87":
        print '\nFOUND KEY:', repr(key)
        break
''' 
key = '\xf7t\xe7'
# flags = [''.join(c) for c in itertools.product('0123456789abcdefghijklmnopqrstuvwxyz_!', repeat=9)]
flag = 'UDCTF{'
enc_flag = 'dac6cc1689dd6b3e516ae082d9430510'

for i in range(9, 0, -1):
    print 'i =', i
    for c in string.digits+string.ascii_letters+string.punctuation:
        # print len(flag + c*i + '}')
        # print flag + c*i + '}'
        ct = cipher(key, flag + c*i + '}')
        if ct[:len(flag+c)*2] == enc_flag[:len(flag+c)*2]:
            # print 'FOUND ********************'
            flag = flag + c
            print flag
            break
flag = flag + '}'
print flag

print sflag(flag)
with open('flag.txt', 'w') as f:
    f.write(sflag(flag))


'''
flags = [''.join(c) for c in itertools.permutations('0123456789abcdefghijklmnopqrstuvwxyz_!', 9)]

for flag in tqdm(flags):
    ct = cipher(key, 'UDCTF{' + flag + '}')
    if ct == 'dac6cc1689dd6b3e516ae082d9430510':
        print '\nFOUND FLAG:', flag
        break
'''
# print cipher(key,'UDCTF{' + 'a'*9 + '}')
 
