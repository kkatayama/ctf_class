curl -si http://udctf.com:5002/ | grep 'part1' | tr '=' ' ' |awk '{print $3}' | html2text
a=$(curl -si http://udctf.com:5002/ | grep 'part1' | tr '=' ' ' |awk '{print $3}' | html2text)

curl -s http://udctf.com:5002/images/ | html2text
curl -s http://udctf.com:5002/images/part2.txt
b=$(curl -s http://udctf.com:5002/images/part2.txt)

curl -si http://udctf.com:5002/ | grep 'part3' | tr '=' ' ' |awk '{print $3}' | html2text
c=$(curl -si http://udctf.com:5002/ | grep 'part3' | tr '=' ' ' |awk '{print $3}' | html2text)

curl -s http://udctf.com:5002/robots.txt
curl -s http://udctf.com:5002/flags/part4
d=$(curl -s http://udctf.com:5002/flags/part4)

curl -s http://udctf.com:5002/flags/part5
e=$(curl -s http://udctf.com:5002/flags/part5)

f="$a$b$c$d$e"

echo "\n\nFLAG = $f"

