# Blocky

FILES: [cipher.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/cipher.py) [ct1](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/ct1) [ct2](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/ct2)

## Initial Analysis 
For this challenge, we were given three files.  A
[cipher.py](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/cipher.py)
script that was used to encrypt two plaintext messages and produce two
ciphertext files:
[ct1](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/ct1)
[ct2](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/blocky/ct2)

#### cipher.py
```python
from Crypto.Cipher import DES
import string
import os

def super_encryption(plaintext, key):
    ct = ""
    cipher = DES.new(key)
    for a_letter in plaintext:
        ct += cipher.encrypt(a_letter*8)
    return ct

with open('flag', 'r') as f:
    flag = f.read().strip()

key = os.urandom(8)
ct1 = super_encryption(string.printable, key)
ct2 = super_encryption(flag, key)

with open('ct1','w') as f:
    f.write(ct1.encode('hex'))

with open('ct2','w') as f:
    f.write(ct2.encode('hex'))
```

#### ct1
```Mask
d030a3d6f33c40c5a6182cf367b0c6d303c2f3b4f6c73b8a305f8d42d26c20b38d6729bd8baf62c547a7b5b3acba0ecc6eb236d38c9b9436ad2f563c5989c371f30d80ca6efde721c94116531e30862e7d82646f3409d1a99918f9871638b86bdbce94a9ade88719822fd6d2e281275fda5d5f0b6d348c4e81e792fc44a98bbb46b7d4b2dacd37ad3a159855569eec981336138f6b302e59d4e1046b603f698d307a90ac9dde97f5fd69b00bfd6676772e8d69c6f561fcfebee3d3b965366d6a7f4e5856ef72d528f7635ade604b5ca49a336905afc372c01ae014b3397963d708eacd81eace57173ad28f06d6362106b5de47633da6bbabcc0d6e73a406e1aa5075302a4f0e6890d5d89376e1078cc522328194870d933263d8f2b2b41cd7be7b4415a6e2cc3563ae178e756572b45f6bc50d71a484c0af55a39071aa4d92d1dbf8b3abdd8f193e795523c3009782f7f85c2f04a0dee9e253f43c28d5123bdbdbe11314ded883d06b2b0a40f675a51049a6eefafae83435441e5795febe7813265cc046a5c30abfc1c0bb06cb35802a07cdeb80d085fb75b14e171547e0e58782ffd4e31f3153713b8b451264a14038ea64b0696a893ba9f4a45a3d549ad2f44e3b56f748fd15812240171ff3866694e80f1fff5c6b0d1fd83835619e58cab17986c6a6dfca578ec514ef24bf9ee05f7f8d409f3c72b5daa26ec3635ebfd3bd564e1019ed73c71a1a9ba9c96375fd3a495ebe17d133a7d57ee30f1c2c5ac0b371263a79874a9e8cd0231dda7ced5e560a85bf52bc48ed94c2cd908d28d4bd53cfbfb30823aef99d908d987edd4a6366ee03610deb6c90fb09f4a37f38b73607357cdef199a052bb13c3c3117fbea68ce09878cbc02d031b979be22483162bfa452feda7f2547f628be5d6a7f115295ba86554180a0e3e3412ed42614954b0662a52915ac8d2eb28bb4026204b9f533588a9e98176f766aab1f302832cefb1e1730ec224853d20b6a4272979ee02a452f1fde15cd882bfcf6333463d0f1ce64a650921975168d427a5b8e288f64cc9d3db6444ff483c0a84290ea2dc19d028be73677879953fe247dcaf920f3a94908449a7b2f55e83e61fba0ebba2c2d37894%
```

#### ct2
```Mask
4e3b56f748fd158155a39071aa4d92d16bc50d71a484c0aff4a45a3d549ad2f4795523c3009782f7f1fde15cd882bfcf5075302a4f0e68903a159855569eec98305f8d42d26c20b3bee3d3b965366d6a730ec224853d20b65075302a4f0e6890a6182cf367b0c6d3fd69b00bfd667677fd69b00bfd667677730ec224853d20b622328194870d9332d030a3d6f33c40c5b5de47633da6bbab730ec224853d20b6fd69b00bfd667677305f8d42d26c20b38d6729bd8baf62c51ae014b3397963d7bee3d3b965366d6a730ec224853d20b63ad28f06d63621063a159855569eec988d6729bd8baf62c53ad28f06d6362106730ec224853d20b622328194870d9332d030a3d6f33c40c5b5de47633da6bbab1ae014b3397963d7730ec224853d20b68d6729bd8baf62c5dbce94a9ade887193ad28f06d6362106a6182cf367b0c6d3d030a3d6f33c40c5bee3d3b965366d6a08eacd81eace5717730ec224853d20b63a159855569eec988d6729bd8baf62c5cc0d6e73a406e1aada5d5f0b6d348c4e730ec224853d20b6dbce94a9ade88719d030a3d6f33c40c5bee3d3b965366d6a08eacd81eace5717305f8d42d26c20b39a336905afc372c0b5de47633da6bbab305f8d42d26c20b3bee3d3b965366d6adbce94a9ade88719305f8d42d26c20b308eacd81eace5717650921975168d427%
```

From the `cihper.py` script, we see that both plaintext messages were
encrypted using `DES Block Cipher` and that each 8 byte block is
filled with the same character.  Our task for this challenge is to use
the known plaintext and how it was encrypted to map and decrypt the unknown
cipher text.

## Tools 
* string (python)
* teddy utilities (my custom python module)

## Computing the Answer 
### Read the ciphertext files
```python
with open('ct1') as f:
    ct1 = f.read().decode('hex')
with open('ct2') as f:
    ct2 = f.read().decode('hex')
```

### Split both ciphertexts into 8-byte blocks
```python
ct1_split = teddy.split_string(ct1, 8)
ct2_split = teddy.split_string(ct2, 8)
```

### Generate the lookup table
```python
lookup_table = {}
for i in range(100):
    lookup_table[ct1_split[i]] = string.printable[i]
```

### Decode the unknown plaintext
```python
plaintext = ''
for ct in ct2_split:
    plaintext += lookup_table[ct]
```

#### hack_blocky.py
```python
import string
import teddy
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

with open('ct1') as f:
    ct1 = f.read().decode('hex')
with open('ct2') as f:
    ct2 = f.read().decode('hex')

ct1_split = teddy.split_string(ct1, 8)
ct2_split = teddy.split_string(ct2, 8)

lookup_table = {}
for i in range(100):
    lookup_table[ct1_split[i]] = string.printable[i]

plaintext = ''
for ct in ct2_split:
    plaintext += lookup_table[ct]

print flag(plaintext)
with open('flag.txt', 'w') as f:
    f.write(flag(plaintext))
```

## Results
```Mask
➜  blocky git:(master) python hack_blocky.py

UDCTF{wh3n_w1ll_y0u_l34rn_th4t_y0ur_4ct10ns_h4ve_c0ns3qu3nc3s}
```

## The Flag 
```ObjectScript
UDCTF{wh3n_w1ll_y0u_l34rn_th4t_y0ur_4ct10ns_h4ve_c0ns3qu3nc3s}
```
