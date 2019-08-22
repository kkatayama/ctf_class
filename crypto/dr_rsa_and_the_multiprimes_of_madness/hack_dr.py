from gmpy2 import mpz, powmod
from rsa_hacked import ct, d, N
from Crypto.Util.number import long_to_bytes

ct = long(ct)
d = long(d)
N = long(N)
pt = powmod(ct, d, N)
with open('plaintext', 'w') as f:
    f.write('pt='+str(pt))
print long_to_bytes(pt)


