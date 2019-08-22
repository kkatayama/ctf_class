# coding: utf-8
from Crypto.Util.number import *
import gmpy2
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

with open('rsa_values') as f:
    values = [l.strip() for l in f]

for val in values:
    print val
    exec(val)

# we have d, ct, n
pt = gmpy2.powmod(ct, d, n)
p = long_to_bytes(pt)

print flag(p)
with open('flag.txt', 'w') as f:
    f.write(flag(p)+'\n')
    
