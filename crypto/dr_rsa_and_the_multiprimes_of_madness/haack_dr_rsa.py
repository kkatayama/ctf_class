# coding: utf-8
from sage.all import *
from GIANT_modulus import ct, e, N

ct = Integer(ct)
e = Integer(e)
N = Integer(N)
        
phi = euler_phi(N)
d = inverse_mod(e, phi)

with open('rsa_hacked.py','w') as f:
    f.write('ct='+str(ct)+'\n')
    f.write('d='+str(d)+'\n')
    f.write('N='+str(N)+'\n')
    
print 'saved d, ct, and N to rsa_hacked.py'
