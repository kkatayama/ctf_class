# coding: utf-8
import itertools
import teddy
import string
# import multiprocessing as mp
import os
from multiprocessing import Pool
from Crypto.Cipher import DES
from tqdm import tqdm, trange

# GLOBALS
chars = ''.join([chr(c) for c in xrange(256)])
# chars = string.printable
# total = 2**32 
total = teddy.get_length_itertools('product', string.digits, 8)
# num_parts = 8
# part_size = len(chars) / num_parts
num_processors = 8
with open('ct1') as f:
    ct1 = f.read().decode('hex')
        
def encrypt(p, k):
    cipher = DES.new(k)
    return cipher.encrypt(p)

def do_job(n): # start_bits):
    chunk = len(chars) / num_processors
    a = (n * chunk)
    b = (n * chunk) + chunk
    text = "processor #{}".format(n)
    try:
        
        # for i in trange(total, desc=text, position=n): # tqdm(itertools.permutations(start_bits, 8), total=total/num_parts):
        for k in tqdm(itertools.product(chars[a:b], repeat=8), total=(total/num_processors), desc=text, position=n):
            # key = os.urandom(8) # str(int('12345671') + n) #
            key = ''.join(k)
            # for key in [kk*2,'00'+kk+'00','0000'+kk, kk+'0000']:
            if encrypt('00000000', key)[0:4] == ct1[0:4]:
                print 'FOUND KEY:', repr(key)
                with open('key','w') as f:
                    f.write(key+'\n')
                    f.write('enc = ' + encrypt('00000000', key).encode('hex') + '\n')
                    f.write('ct1 = ' + ct1[0:8].encode('hex') +'\n')
                return key
    except KeyboardInterrupt:
        p.terminate()
        p.join()
        
if __name__ == '__main__':
    L = list(range(num_processors))
    p = Pool(len(L))
    p.map(do_job, L)
    print '\n' * (len(L) - 2)
    keys = []   
    '''
    pool = mp.Pool()
    results = []
    for i in xrange(num_parts):
        if i == num_parts - 1:
            start_bit = chars[part_size * i :]
        else:
            start_bit = chars[part_size * i : part_size * (i+1)]
        results.append(pool.apply_async(do_job(start_bit, i)))

    pool.close()
    pool.join()
    '''

