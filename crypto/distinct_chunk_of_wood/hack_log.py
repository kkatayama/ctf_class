# coding: utf-8
from sage.all import *
from binascii import unhexlify
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

p = Integer(122488473105892538559311426995019720049507640328167439356838797108079051563759027212419257414247)
g = Integer(2)
h = Integer(70388135743471424569479456639590418870801238093684057816981773116569876008168393577185261489015)

R = IntegerModRing(p)
x = discrete_log(R(h), R(g))

temp = unhexlify(x.hex())
print flag(temp)

with open('flag.txt', 'w') as f:
    f.write(flag(temp))
