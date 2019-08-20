echo '\nexamining site...\n'
cmd="curl -si http://udctf.com:5004/"
echo $cmd
$cmd

echo '\nclicking around site...\n'
cmd="curl -sL http://udctf.com:5004/?page=1 | html2text"
echo '\n'
echo $cmd
$cmd

cmd="curl -sL http://udctf.com:5004/?page=2 | html2text"
echo '\n'
echo $cmd
$cmd

cmd="curl -sL http://udctf.com:5004/?page=3 | html2text"
echo '\n'
echo $cmd
$cmd

echo '\ntrying 1000 pages...\n'
cmd="curl -s http://udctf.com:5004/\?page=\[1-1000\] | html2text -unparse | grep --color=auto -a -E 'UDCTF{.*?}'"
echo $cmd'\n'
curl -s http://udctf.com:5004/\?page=\[1-1000\] | html2text -unparse | grep --color=auto -a -E 'UDCTF{.*?}'
f=$(curl -s http://udctf.com:5004/\?page=\[1-1000\] | html2text -unparse | grep --color=auto -a -E 'UDCTF{.*?}')

echo $f > flag.txt
echo '\n'
