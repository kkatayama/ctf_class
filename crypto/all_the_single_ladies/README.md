# All_The_Single_Ladies
2<sup>8</sup> is a pretty big search space, right?

FILE: `output.txt`

## Initial Analysis 
For this challenge, we were given an encrypted binary file, `output.txt`.

Our goal is to decrypt the message contained in the file.
> Provided Hint: XOR challenge with 2<sup>8</sup> search space.

## Tools 
* xor() from pwn-tools


## Computing the Answer 

### Read the binary file
```python
with open('output.txt', 'rb') as f:
    ct = f.read()
```

### XOR the ciphertext with the hinted search space
```python
for c in range(0, 256):
    pt = xor(chr(c), ct)
    if 'UDCTF' in pt:
        temp = pt.split('flag: ')[1]
        print pt.split('flag: ')[0]
        break
```

#### hack_single_ladies.py
```python
from pwn import xor
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

with open('output.txt', 'rb') as f:
    ct = f.read()

for c in range(0, 256):
    pt = xor(chr(c), ct)
    if 'UDCTF' in pt:
        temp = pt.split('flag: ')[1]
        print pt.split('flag: ')[0]
        break

print flag(temp)
with open('flag.txt', 'w') as f:
    f.write(flag(temp))

```

### Results
```Mask
➜  all_the_single_ladies git:(master) ✗ python hack_single_ladies.py

A took a byte out of Gottfreid's sandwich, while he wasn't looking. Thank
God I encrypted this, he'll never know the atrocities I committed, including stealing his
UDCTF{i'll_never_get_to_take_a_byte_out_of_a_jimmy_john's_sandwich_again_RIP_Jimmy_Johns} and stealing calculus.
```

## The Flag 
```ObjectScript
UDCTF{i'll_never_get_to_take_a_byte_out_of_a_jimmy_john's_sandwich_again_RIP_Jimmy_Johns}
```
