# coding: utf-8
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

with open('ct') as f:
    ct = f.read().strip()
with open('flags.txt') as f:
    flags = [l.strip() for l in f]

the_flag = ''
size = 32

for i in range(0, len(ct), size):
    chunk = ct[i:i+size]
    print '\n' + chunk
    print '-'*100
    for line in flags:
        line = line.split(':')
        temp = line[0]
        h_ct = line[1]
        if chunk in h_ct:
            h_index = h_ct.find(chunk)
            f_index = h_index / 2
            print h_ct[h_index:h_index+size]# h_ct[i:i+size]
            print temp[f_index:f_index+(size/2)] # temp[(i/2):(i/2)+(size/2)]
            print temp
            print h_ct
            the_flag += temp[f_index:f_index+(size/2)]
            break
print '\n'
print '*'*100
print ct
print '\n' + flag(the_flag)

with open('flag.txt', 'w') as f:
    f.write(flag(temp))
