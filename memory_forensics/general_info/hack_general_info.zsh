#!/usr/local/bin/zsh

flag=$(vol.py -v -f ~/ctf_tools/OtterCTF.vmem --profile=Win7SP1x64 printkey -o 0xfffff8a000024010 -K "ControlSet001\Control\ComputerName\ComputerName" | grep -ia "ComputerName    : (S)" | cut -d' ' -f15)
echo "\nUDCTF{${flag}}"
echo -n "UDCTF{${flag}}" > flag.txt
