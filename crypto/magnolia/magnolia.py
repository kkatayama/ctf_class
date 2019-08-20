N = 4857667584940312213039485766758494031221303948576675849403122130394857667584940312213039485766758494031221303948576675849403122130394857667584942646052215059687786960514233241505968778696051423324150596877869605142332415059687786960514233241505968778696051423324150596877869605142332415059687806358441041
e = 65537
 

FLAG = "REDACTED" 
from Crypto.Util.number import *
from gmpy2 import next_prime

rep = gmpy2.next_prime(2**1000) 
def encrypt_me(pt):
    ciphertext = bytes_to_long(pt) 
    for i in range(rep): 
        ciphertext = pow(ciphertext, e, N)
    return ciphertext

def main(): 
    with open('output.py', 'w') as f: 
        f.write('ct = {}'.format(encrypt_me(FLAG))) 

if __name__ == '__main__': 
    main() 
