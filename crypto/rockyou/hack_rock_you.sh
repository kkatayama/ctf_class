echo "hashcat -m 1400 leaked.txt ../../web/leaked_db/crackstation.txt -r rules --debug-mode=1 --debug-file=matched.rule -O"
hashcat -m 1400 leaked.txt ../../web/leaked_db/crackstation.txt -r rules --debug-mode=1 --debug-file=matched.rule -O

flag=$(hashcat -m 1400 leaked.txt ../../web/leaked_db/crackstation.txt -r rules --debug-mode=1 --debug-file=matched.rule -O --show | egrep -v '\{[0-9]+\}' | cut -d':' -f2 | cut -d'{' -f 2 | cut -d'}' -f 1)
echo "\033[96mUDCTF\033[00m""\033[92m{\033[00m""\033[91m${flag}\033[00m""\033[92m}\033[00m"
echo "\033[96mUDCTF\033[00m""\033[92m{\033[00m""\033[91m${flag}\033[00m""\033[92m}\033[00m" > flag.txt
