# coding: utf-8
import codecs
import string
from teddy import split_string
from pwn import *
from Crypto.Util.number import *

with open('ct') as f:
    cts = [codecs.decode(l.strip(), 'hex') for l in f]
cts.pop(2)

salt = codecs.decode(b'7574666c61677b', 'hex')
for i, ct in enumerate(cts):
    print('{}: '.format(i), end='')
    # for j in range(20, 128):
    #     print(chr(j).encode(), xor(salt + b'tw0_tim3_p4ds}utflag{tw0_tim3_p' +chr(j).encode(), ct))    
    print(xor(salt+b'tw0_tim3_p4ds}utflag{tw0_tim3_p', ct).decode())
