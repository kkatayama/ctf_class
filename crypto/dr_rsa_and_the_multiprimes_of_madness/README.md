# DR_RSA_and_the_Multiprimes_of_Madness

My friend just sent me an encrypted message along with the values <i>d</i> and <i>n</i>. I'm not sure what to do with them.

FILE: [GIANT_modulus.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/dr_rsa_and_the_multiprimes_of_madness/GIANT_modulus.py)

## Initial Analysis 

For this challenge, we were given a file [GIANT_modulus.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/dr_rsa_and_the_multiprimes_of_madness/GIANT_modulus.py) that contained RSA parameters.  The parameter for `e` was 65537.  Parameters `ct`, and `N` are huge so instead of displaying them here, please reference the `GIANT_modulus.py` file to see them.

## Tools 
* gmpy2 (python)
* sage (python)

## Computing the Answer 
### Read the RSA parameters from `GIANT_modulus.py` file
```python
from sage.all import *
from GIANT_modulus import ct, e, N

ct = Integer(ct)
e = Integer(e)
N = Integer(N)
```

### Compute `phi` and `d` using sage
```python
phi = euler_phi(N)
d = inverse_mod(e, phi)
```

### Decrypt the ciphertext using gmpy2
```python
pt = gmpy2.powmod(ct, d, n)
p = long_to_bytes(pt)
```

#### hack_dr_rsa.py
```python
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
```

#### hack_dr.py
```python
from gmpy2 import mpz, powmod
from rsa_hacked import ct, d, N
from Crypto.Util.number import long_to_bytes

ct = long(ct)
d = long(d)
N = long(N)
pt = powmod(ct, d, N)
with open('flag.txt', 'w') as f:
    f.write(long_to_bytes(pt))
print long_to_bytes(pt)
```

### RESULTS
```Mask
➜  dr_rsa_and_the_multiprimes_of_madness git:(master) ✗ sage -python haack_dr_rsa.py

saved d, ct, and N to rsa_hacked.py

➜  dr_rsa_and_the_multiprimes_of_madness git:(master) ✗ python hack_dr.py

UDCTF{phee_PHI_pho_phum_coming_up_w_flags_is_hard_and_I_am_dumb!!!!!}
```


## The Flag 
```ObjectScript
UDCTF{phee_PHI_pho_phum_coming_up_w_flags_is_hard_and_I_am_dumb!!!!!}
```
