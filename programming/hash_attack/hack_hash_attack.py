# coding: utf-8
from pwn import *
from hashid import HashID  # https://github.com/psypanda/hashID
import hashlib
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

def get_hash(msg, dictionary):
    hash_id = HashID()
    hash_type = hash_id.identifyHash(msg).next().name.lower().replace('-', '')
    with open(dictionary) as f:
        for word in f:
            test_hash = eval("hashlib." + hash_type +"(word.strip()).hexdigest()")
            if test_hash == msg:
                return word.strip()

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

### START HACK ###
r = remote('3.220.181.160', 6002)
cond = '\n'
m = s('', cond, '')

found = False
while not found:
    if 'UDCTF{' in m:
        found = True
    elif cond in m:
        if m.count(cond) == 1:
            m_hash = m.split(cond)[0]
        else:
            m_hash = m.split(cond)[1]
        ans = get_hash(m_hash, 'dictionary.txt')
        m = s(ans, cond, 'send')


temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
