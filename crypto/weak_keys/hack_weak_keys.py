# coding: utf-8
from Crypto.Util.number import *
from pwn import *
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

with open('ciphertext') as f:
    ct = f.read()
    
with open('encrypt.py') as f:
    ec = f.read()

iv =  '1l0v3ctf'
ind = 'We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness'

print xor(ct.decode('hex'), ind+iv)
print repr(xor(ct.decode('hex'), ind+iv))
print xor(ct.decode('hex'), '\xe8\xdd61\xfe\x8e\x91.'+iv)

temp = xor(ct.decode('hex'), '\xe8\xdd61\xfe\x8e\x91.'+iv)
print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
