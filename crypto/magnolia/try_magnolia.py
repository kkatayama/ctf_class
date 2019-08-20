# coding: utf-8
def fermat(n):
    x = gmpy2.ceil(gmpy2.sqrt(n))
    y = x**2 - n
    while not gmpy2.sqrt(y).is_integer():
        x += 1
        y = x**2 - n
    return x + gmpy2.sqrt(y), x - gmpy2.sqrt(y)
p, q = fermat(N)
phi = (p-1)*(q-1)
d = gmpy2.invert(e, long(phi))
pt = long(ct)
i = 0
while i < rep:
    pt = gmpy2.powmod(pt, long(d), long(p*q))
    i += 1
print pt
print long_to_bytes(pt)
# print long_to_bytes(gmpy2.powmod(ct, long(d), long(p*q)))
    
