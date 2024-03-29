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

        
