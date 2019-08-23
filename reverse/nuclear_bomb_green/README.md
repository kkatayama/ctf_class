# Nuclear_Bomb_Green

You must defuse Dr. Von Noizeman's nuclear bomb!

The flag for this challenge is the answer for the `green` wire, wrapped in the `UDCTF{}` flag format.

Please see the Nuclear Bomb: Yellow challenge for the bomb executable.

FILE: [bomb](https://github.com/kkatayama/ctf_class/blob/master/reverse/nuclear_bomb_green/bomb?raw=true)

## Initial Analysis 
For this challenge, we were given a binary file [bomb](https://github.com/kkatayama/ctf_class/blob/master/reverse/nuclear_bomb_green/bomb?raw=true).
This time we have to enter the correct password to `Disengage` the green wire.

![intro](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_green/intro.png)

## Tools 
* radare2 (bash)
* cutter (osx GUI for radare2)

## Computing the Answer 
### Debugging

![verify](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_green/verify.png)

At first glance, it was clear that the password being checked is `dcaotdae`.  However, after entering that password, the lock `Disengaged` the green wire for just a few seconds and then crash after re-engaging.
Looking closer at the steps following the password check I noticed that there is a bit-wise `AND` operation following the `Noizev Re-engage` that causes the jump to seg fault.

```Mask
0x08049936      c70424c0a204.  dword [esp] = str.dcaotdae    ; obj.password ; [0x804a2c0:4]=0x6f616364 ; "dcaotdae"
0x0804993d b    e892eeffff     sym.imp.strncmp ()          ;[1] ; int strncmp(const char *s1, const char *s2, size_t n)
0x08049942      85c0           var = eax & eax
0x08049944 b    7548           if (var) goto 0x804998e     ;[2]
0x08049946 b    c70424fca204.  dword [esp] = str.e_42m__e_0m_e_32m_UNLOCK_PASSWORD_2_ACCEPTED__LOCK_DISENGAGED_e_0m    ; [0x804a2fc:4]=0x32345b1b
```
This `AND` operation is computed with the last bit of the last input character `e` which in binary `01100101` ends with a `1`.  Seeing that the password only checks the characters up to `n` 
I padded the password with some `0`'s.

### RESULTS
![hack](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_green/hack1.png)![hack](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_green/hack.png)


## The Flag 
```ObjectScript
UDCTF{dcaotdae000}
```
