from Crypto.Cipher import DES
with open('key', 'r') as f:
    key = f.read().strip().decode('hex')
    
with open('message', 'r') as f:
    msg = f.read().strip()
    
iv = '1l0v3ctf'
cipher = DES.new(key, DES.MODE_OFB, iv)
ct = cipher.encrypt(msg)
with open('ciphertext', 'w') as f:
    f.write(ct.encode('hex'))
    
