# coding: utf-8
from Crypto.Util.number import *
from pwn import *
import gmpy2
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

def fermat(n):
    x = gmpy2.ceil(gmpy2.sqrt(n))
    y = x**2 - n
    while not gmpy2.sqrt(y).is_integer():
        x += 1
        y = x**2 - n
    return x + gmpy2.sqrt(y), x - gmpy2.sqrt(y)

with open('rsa_values') as f:
    values = [l.strip() for l in f]

for val in values:
    print val
    exec(val)

'''
c = 16616401862970117262211667400956073423834792078483318828719359790277372651094615175520467274373914465566367947954338095267385644045181394104396864955022428882295298060406384226930006890837455901487274279875048819165079804283242322683756468643792258515287131814805429624443600787445529565074140761126872596128108425802971166249105560346601058190714947895826003200420593747054086145959772327542491136341577305637950621916292654724299373486076721139593540374341083561230560836185785964795646293271301933377104508701305218613813820610570366467237517044658441617527279042438873376723195785459718046627806032542916628965599
N = 29066625938753234623753553050845262847384494092460329512875312793404046479347832518744672541186665961375466775506202288641451900291392517594213604285705683364229918598405716671951919712108247053015725208790173735774195390602377206455254142198962424200879337128121634329849698138762752948803937755691553326350946908528283009205260072695949349816017374841322650241647938728987811046013821522504492115353173639763181876772327463102556924927933158760586124088570057489209767094296767033449522944394186681923255263512078872642617770701640254325027442723007313064006528626445761761211039090172983225602683948049752389515731
e = 65537
'''

p, q = fermat(n)
phi = (p-1)*(q-1)
d = gmpy2.invert(e, long(phi))
print long_to_bytes(gmpy2.powmod(ct, long(d), long(p*q)))

# check if N is prime
# if not isPrime(N):
