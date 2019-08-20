from Crypto.PublicKey import RSA
import signal
import gmpy2
from libnum import *
import requests
import re
import argparse
import os
import subprocess
from glob import glob

def red(prt):
    return "\033[91m{}\033[00m".format(prt)
def grn(prt):
    return "\033[92m{}\033[00m".format(prt)
def cyn(prt):
    return "\033[96m{}\033[00m".format(prt)
def flag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('UDCTF', cyn('UDCTF')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))

from binascii import unhexlify
from operator import mul

def is_sqrt(number):
    x = number
    y = (x + number // x) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2
    return x

def isqrt(n):
    return int(n**.5)


def fermat(n, verbose=False):
    a = is_sqrt(n)
    b2 = a ** 2 - n
    b = isqrt(n)
    count = 0
    while b ** 2 != b2:
        if verbose:
            print('%s. Trying: a=%s b2=%s b=%s' % (count, a, b2, b))
        a += 1
        b2 = a ** 2 - n
        b = isqrt(b2)  
        count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def crack(n, e, c, output_type='str'):
    p, q = fermat(n)
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    if output_type == 'int':
        return m
    elif output_type == 'str':
        m = str(hex(m))[2:-1].decode("hex")
        return m
    elif output_type == 'hex':
        m = str(hex(m))[2:-1]
        return m


# Edit it, if you want
C=16616401862970117262211667400956073423834792078483318828719359790277372651094615175520467274373914465566367947954338095267385644045181394104396864955022428882295298060406384226930006890837455901487274279875048819165079804283242322683756468643792258515287131814805429624443600787445529565074140761126872596128108425802971166249105560346601058190714947895826003200420593747054086145959772327542491136341577305637950621916292654724299373486076721139593540374341083561230560836185785964795646293271301933377104508701305218613813820610570366467237517044658441617527279042438873376723195785459718046627806032542916628965599
N=29066625938753234623753553050845262847384494092460329512875312793404046479347832518744672541186665961375466775506202288641451900291392517594213604285705683364229918598405716671951919712108247053015725208790173735774195390602377206455254142198962424200879337128121634329849698138762752948803937755691553326350946908528283009205260072695949349816017374841322650241647938728987811046013821522504492115353173639763181876772327463102556924927933158760586124088570057489209767094296767033449522944394186681923255263512078872642617770701640254325027442723007313064006528626445761761211039090172983225602683948049752389515731
e=65537

# print crack(n, e, c)
# Factor N and compute d
print("[+] Computing d...")
UPF = list(factor(N))                           # Unique Prime factorization
phi_fs = [pow(p, k-1) * (p-1) for p, k in UPF]  # phi for each factor
factors = [pow(p, k) for p, k in UPF]           # The raw factors of N
d = inverse_mod(e, reduce(mul, phi_fs, 1))      # Private exponent

# Use CRT to compute d rather than the fast-power algorithm
print("[+] Doing CRT to compute M...")
M = CRT_list(
    [int(pow(C, d % p_i, f_i)) for p_i, f_i in zip(phi_fs, factors)],
    [N / f_i for f_i in factors]
)

# Flag
print("[+] FLAG: {sflag}".format(sflag=unhexlify(hex(M))))
print flag(unhexlify(hex(M)))

with open('flag.txt', 'w') as f:
    f.write(flag(unhexlify(hex(M))))
           
