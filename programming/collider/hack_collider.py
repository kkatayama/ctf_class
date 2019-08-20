# coding: utf-8
from pwn import *
from itertools import product
import string
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

def get_hash(msg_line):
    line = msg_line.strip()
    h_type = line.split('[')[0]
    h_sect = int(line.split(':')[1].split(']')[0])
    h_line = line.split(' is ')[1]
    # print h_type, h_sect, h_line
    
    cracked = False
    p = log.progress('running dictionary attack...')
    ### Try Dictionary Attack ###
    while not cracked:
        for cc in dictionary:
            c = cc.strip()
            if h_type == 'md5':
                test_hash = hashlib.md5(c).hexdigest()[:h_sect]
            else:
                test_hash = hashlib.sha1(c).hexdigest()[:h_sect]
            if test_hash == h_line:
                cracked = True
                p.success('cracked: ' + c)
                break
    i = 1
    p.status('trying brute force...')
    ### Try Brute Force ###
    while not cracked or i == 6:                
        for cc in product([chr(j) for j in range(256)], repeat = i):
            c = ''.join(cc)
            if h_type == 'md5':
                test_hash = hashlib.md5(c).hexdigest()[:h_sect]
            else:
                test_hash = hashlib.sha1(c).hexdigest()[:h_sect]
            if test_hash == h_line:
                cracked = True
                p.success('cracked: ' + c)
                break
        i += 1
    p.failure('could not find hash: ' + h_line)
    return c

def s(stuff, condition, status):
    if status == 'send':
        log.info('sending: ' + stuff)
        msg = r.sendlinethen(condition, stuff, timeout=0.5)
    else:
        msg = r.recvuntil(condition, timeout=0.5)
    log.indented('\n')
    log.info('received: ' +  msg)
    return msg

with open('dictionary.txt') as f:
    dictionary = [l.strip() for l in f]
with open('rockyou.txt') as f:
    rockyou = [l.strip() for l in f]
dictionary.extend(rockyou)
    
### START HACK ###
r = remote('52.15.140.126', 6969)
cond = '\n'
m = s('', cond, '')

found = False
while not found:
    if 'UDCTF{' in m:
        found = True
    elif cond in m:
        if m.count(cond) == 1:
            m_line = m.split(cond)[0].split('Find a string such that ')[1]            
        else:
            m_line = m.split(cond)[1].split('Find a string such that ')[1]
        ans = get_hash(m_line)
        m = s(ans, cond, 'send')


temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
