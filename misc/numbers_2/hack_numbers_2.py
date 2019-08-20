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


aa = '11001111111111100011111111110011101100'
ab = '110011010111011110011001010100010101010'
a_ = int(aa.zfill(40),2)
a__ = int(ab.zfill(40),2)
a = xor(long_to_bytes(a_), long_to_bytes(a__))

bb = '34754671171482463'
b = long_to_bytes(bb)

cc = [109, 52, 115, 116, 51]
c = long_to_bytes(bytes_to_long("".join(map(chr, cc))))

dd = '7233645f74'
d = dd.decode('hex')

ea = '\xf9 \xdcu\x9ef\xbbHso{'
eb = '\x91\x11\xaf*\xf2U\xc8;C\x01\x06'
e = xor(ea, eb)

temp =  a+b+c+d+e
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
