# Distinct_Chunk_of_Wood

FILE: [log.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/distinct_chunk_of_wood/log.py)

## Initial Analysis 
For this challenge, we wre given a python script  [log.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/distinct_chunk_of_wood/log.py) containing the parameters use to encrypt the secret plaintext.

#### log.py
```python
from Crypto.Util.number import *
from secret import flag

x = bytes_to_long(flag)
p = 122488473105892538559311426995019720049507640328167439356838797108079051563759027212419257414247
g = 2

h = pow(g, x, p)
print h
# 70388135743471424569479456639590418870801238093684057816981773116569876008168393577185261489015
```

From the file we are given the parameters `p`, `g`, and `h`.  Our task for this challenge is to decrypt the message by computing `x`. 

## Tools 
* IntegerModRing() (sage)
* Integer() (sage)
* discrete_log() (sage)
* unhexlify() from binascii (python)

## Computing the Answer 

### Generate rings
```python
R = IntegerModRing(p)
R.factored_unit_order()

[2 * 3485548229,
 2 * 37561 * 3485548229,
 2 * 35491 * 37561 * 3485548229,
 2 * 35491 * 36187 * 37561 * 3485548229,
 2 * 35491 * 36187 * 37561 * 63853 * 3485548229]
```

### Compute discrete log of field with given parameters `g` and `h`
```python
x = discrete_log(R(h), R(g))
```

#### hack_log.py
```python
from binascii import unhexlify
import re

def red(prt):
    return "\033[91m{}\033[00m".format(prt)
def grn(prt):
    return "\033[92m{}\033[00m".format(prt)
def cyn(prt):
    return "\033[96m{}\033[00m".format(prt)
def flag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('UDCTF', cyn('UDCTF')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))

p = Integer(122488473105892538559311426995019720049507640328167439356838797108079051563759027212419257414247)
g = Integer(2)
h = Integer(70388135743471424569479456639590418870801238093684057816981773116569876008168393577185261489015)

R = IntegerModRing(p)
x = discrete_log(R(h), R(g))

temp = unhexlify(hex(x))
print flag(temp)

with open('../School/ctf_class/crypto/distinct_chunk_of_wood/flag.txt', 'w') as f:
    f.write(flag(temp))
```

### RESULTS
```Mask
➜  distinct_chunk_of_wood git:(master) ✗ sage hack_log.py

UDCTF{hi}
```

## The Flag 
```ObjectScript
UDCTF{hi}
```
