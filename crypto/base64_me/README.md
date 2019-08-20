# Base64_Me
I <i>really</i> like base64.

FILE: [flag.b64](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/base64_me/flag.b64)

## Initial Analysis 
For this challenge, we were given a base64 encoded file, [flag.b64](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/base64_me/flag.b64)

Our goal is to decrypt the message contained in the file.

### Test Run
```Mask
➜  base64_me git:(master) ✗ base64 --decode --input=flag.b64 | tail -b 1

R1JVWWxaYVNGVXhhRzlYUm1SSVZXczVWMDFHV2pOV01WcHpWbFpPY1ZWdGFGTmlSbkEyVm1wSk1XRXlSa2RUYms1cVVteHdWMVJYTlZKa01WcHlWMjFHYW1KSFVqRlpWVnByWVZaa1NHRkVTbGRpV0VKSVZYcEdZV1JHVW5KaFJrSlhZbFpLV2xaVVFsZFRNVTVYVjI1R1ZGZEhhRmhVVmxwelRrWmFTRTVWT1doV2EydzFXVlZhVTFkdFJYaFhhazVoVWpOb2FGVnFSbUZqTVZKeldrVTFWMkpZWTNkV2JYQkxUVWRGZUZwRmFGUmhNbWhYV1d0a2IxbFdXWGRoUlU1WVVteHNNMVl5TVVkaE1VbDRVMnRzWVZKV2NHaFdSM2hoWkZaR2NtTkdhR2xTYkhCdlZsaHdSMWR0VmtkYVNGWlZZa1UxYjFsWWNGZFdNVnBIVjJ4a1YyRjZWbGhXYlhSclZURmFTR1ZHU2xkV2JFWXpWREZGT1ZCUlBUMD0=%
```
> After one run of `base64 --decode` the output is also encoded in
> base64.  Looks like we need to run several cycles.

## Tools 
* b64decode() from base64 (python)
* base64 (shell)

## Computing the Answer 
### Read the base64 encoded file
```python
with open('flag.b64', 'rb') as f:
    raw = f.read()
```

### Cycle base64 decode
```python
found = 0
while not found:
    tmp = base64.b64decode(raw)
    if 'UDCTF' in tmp:
        print 'FLAG FOUND:', flag(tmp)
        with open('flag.txt', 'w') as f:
            f.write(flag(tmp))
        found = 1
    else:
        raw = tmp
```

#### hack_base64_me.py
```python
import base64
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

with open('flag.b64', 'rb') as f:
    raw = f.read()

found = 0
while not found:
    tmp = base64.b64decode(raw)
    if 'UDCTF' in tmp:
        print 'FLAG FOUND:', flag(tmp)
        with open('flag.txt', 'w') as f:
            f.write(flag(tmp))
        found = 1
    else:
        raw = tmp
```

### Results
```Mask
➜  base64_me git:(master) ✗ python hack_base64_me.py

FLAG FOUND: UDCTF{3nc0d3_4nd_3nc0d3_4nd_3nc0d3_4nd_d3c0d3_4nd_d3c0d3_4nd_d3c0d3}
```

## The Flag 
```ObjectScript
UDCTF{3nc0d3_4nd_3nc0d3_4nd_3nc0d3_4nd_d3c0d3_4nd_d3c0d3_4nd_d3c0d3}
```
