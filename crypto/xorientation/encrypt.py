def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

with open('message.txt', 'r') as f:
    msg = ''.join(f.readlines()).rstrip('\n')

with open('key.txt', 'r') as k:
    key = ''.join(k.readlines()).rstrip('\n')


assert key.isalnum() and (len(key) == 8)
assert 'UDCTF' in msg

with open('encrypted.txt', 'w') as fo:
    fo.write(xor(msg, key))
