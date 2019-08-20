rabin2 -s split32 | grep usefulFunction
echo 039 0x00000649 0x08048649  LOCAL   FUNC   25 usefulFunction
dmesg | grep split32
echo [924525.590562] split32[27464]: segfault at 6161616c ip 000000006161616c sp 00000000ff89f180 error 14 in libc-2.27.so[f7cfe000+1d5000]
