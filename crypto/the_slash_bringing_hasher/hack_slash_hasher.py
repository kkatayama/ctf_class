# coding: utf-8
from hashlib import sha256
import hashlib
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

with open('hash.txt') as f:
    hashes = [l.strip() for l in f]
    
cracked = {}
for i in string.printable:
    h = sha256(i).hexdigest()
    if h in hashes:
        print 'cracked:', i, '=', h
        cracked[h] = i 
temp = ''
for key in hashes:
    try:
        f = cracked[key]
        temp += f
        print flag(temp)
        with open('flag.txt','w') as f:
            f.write(flag(temp))
    except:
        pass
    
