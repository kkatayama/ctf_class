# coding: utf-8
from pwn import *
from hashid import HashID  # https://github.com/psypanda/hashID
import itertools
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

def get_hash(msg):
    h_line = msg.split()[-1:][0].strip('?')
    h_type = h_line.split('(')[0]
    h_word = h_line.split('(')[1].rstrip(')')
    if h_type == 'sha1':
        return hashlib.sha1(h_word).hexdigest()
    else:
        return hashlib.sha256(h_word).hexdigest()
    
def get_word(msg):
    h_line = msg.split(' == ')[1].split(',')[0]
    h_type = msg.split('(word)')[0].split()[-1:][0]
    with open('dictionary.txt') as f:
        words = [l.strip() for l in f]

    # print h_line, h_type
    for word in words:
        if h_type == 'sha256':
            test_hash = hashlib.sha256(word).hexdigest()
        else:
            test_hash = hashlib.md5(word).hexdigest()
        if test_hash == h_line:
            return word

    for w in itertools.product(string.printable, repeat=4):
        word = ''.join(w)
        if h_type == 'sha256':
            test_hash = hashlib.sha256(word).hexdigest()
        else:
            test_hash = hashlib.md5(word).hexdigest()
        if test_hash == h_line:
            break
    return word

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
r = remote('52.15.140.126', 7001)
cond = ' >'
m = s('', cond, '')

found = False
while not found:
    if 'UDCTF{' in m:
        found = True
    elif cond in m:
        m_line = m.split(cond)[0].replace('\n', '')
        if 'word' not in m_line:
            ans = get_hash(m_line)
        else:
            ans = get_word(m_line)
        m = s(ans, cond, 'send')


temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
