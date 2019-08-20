# coding: utf-8
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

raw = '383d28313f160c033a4905265a3a1d5c1d051126004d0056260000340e4a14260755170a260e0b49181e0318'

# print xor(raw.decode('hex'), 'mykey')
temp = xor(raw.decode('hex'), 'mykey') # str('UDCTF{'*(len(raw.decode('hex'))/6)+' }').encode('hex')

print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
