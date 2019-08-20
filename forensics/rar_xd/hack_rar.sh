strings -a -n 10 secret.jpg | grep "\S"
convert secret.jpg actual.jpg
hexdump -C secret.jpg | grep "ff d9"
xxd -c1 -p secret.jpg | tr "\n" " " | sed -n -e 's/.*\( ff d9 \)\(.*\).*/\2/p' | xxd -r -p > test.rar
unrar e -p1234 test.rar
cat flag.txt.txt
