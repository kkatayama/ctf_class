# coding: utf-8
from sage.all import *
from GIANT_modulus import ct, e, N

ct = Integer(ct)
e = Integer(e)
N = Integer(N)
        
phi = euler_phi(N)
d = inverse_mod(e, phi)
