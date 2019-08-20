# coding: utf-8
from pwn import xor
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

with open('output.txt', 'rb') as f:
    ct = f.read()

for c in range(0, 256):
    pt = xor(chr(c), ct)
    if 'UDCTF' in pt:
        temp = pt.split('flag: ')[1]
        print pt.split('flag: ')[0]
        break

print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
