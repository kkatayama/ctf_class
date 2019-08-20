# coding: utf-8
import string
import teddy
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

with open('ct1') as f:
    ct1 = f.read().decode('hex')
with open('ct2') as f:
    ct2 = f.read().decode('hex')

ct1_split = teddy.split_string(ct1, 8)
ct2_split = teddy.split_string(ct2, 8)

lookup_table = {}
for i in range(100):
    lookup_table[ct1_split[i]] = string.printable[i]

plaintext = ''
for ct in ct2_split:
    plaintext += lookup_table[ct]

print flag(plaintext)
with open('flag.txt', 'w') as f:
    f.write(flag(plaintext))

