echo '\nexamining site...\n'
curl -si http://udctf.com:5003

echo '\npayload = ./flag.php\n'
curl -s http://udctf.com:5003/flag.php | html2text
f=$(curl -s http://udctf.com:5003/flag.php | html2text)
echo $f
