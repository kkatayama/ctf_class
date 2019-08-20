from pwn import *
from Crypto.Util.number import *
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

def save(obj, filename):
    with open(filename, 'wb') as f:
        f.write(obj)
        
a = 'VURDVEZ7dw=='
a_ = a.decode('base64')

b = '6834745f643033'
b_ = b.decode('hex')

c = '32474288332158060'
c_ = long_to_bytes(c)

d = '01542766646315067137'
d_ = long_to_bytes(int(d, 8))

e = '1000010001101000111001100110001011011000011111101111101'
e_ = long_to_bytes(int(e, 2))

temp =  a_+b_+c_+d_+e_
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
