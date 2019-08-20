# coding: utf-8
from pwn import *
from Crypto.Util.number import *
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
def flag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('UDCTF', cyn('UDCTF')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))

with open('encrypted.txt') as f:
    ct = f.read().strip()

def xor2(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

for i in range(len(ct)-8):
    k = ct[i:i+8]
    test = xor2('UDCTF', k)
    print test
for i in range(len(ct)-8):
    k = ct[i:i+8]
    test = xor2('UDCTF{', k)
    print test
for i in range(len(ct)-8):
    k = ct[i:i+8]
    test = xor2('XORISF', k)
    print test

temp = xor2(ct, 'XORISFUN')
print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))

