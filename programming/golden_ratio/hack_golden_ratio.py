# coding: utf-8
from pwn import *
import gmpy2
import math
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
    
def s(stuff, condition):
    r.sendline(stuff)
    msg = ''
    while condition not in msg and 'UDCTF' not in msg:
        while r.can_recv(timeout=0.1):
            msg += r.recv()
            print msg
    return msg

r = remote('52.15.140.126', 6002)
m = ''
while r.can_recv(timeout=0.5):
    m += r.recv()
print m

cond = 'FIND THE FIB('
found = False
while not found:
    if 'UDCTF{' in m:
        found = True
    elif cond in m:
        n = m.split(cond)[1].split(')')[0]
        ans = str(gmpy2.fib(int(n)) % 10007)
        m = s(ans, cond)

temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))
