# coding: utf-8
from Crypto.Util.number import *
from pwn import *
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

temp = 'UDCTF{'
chars = string.printable
found = 0
while (found != 1):
    for char in chars:
        # print char
        r = remote('3.220.181.160', 6003)
        msg = r.recv()
        enc = msg.split(': ')[1].split('\n')[0]
        # print enc
        r.sendline(temp + char)
        res = r.recv()
        ct = res.split(': ')[1].split('\n')[0]
        # print ct
        if ct in enc:
            temp += char
            print temp
            if '}' in temp:
                found = 1
                flag(temp)
            r.close()
            break
        r.close()
        
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
