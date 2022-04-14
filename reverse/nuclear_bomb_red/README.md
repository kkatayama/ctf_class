# Nuclear_Bomb_Red

You must defuse Dr. Von Noizeman's nuclear bomb!
<p>The flag for this challenge is the answer for the <font color="red"><b>red</b></font> wire, wrapped in the <b>UDCTF{}</b> flag format.</p>

FILE: [bomb](https://github.com/kkatayama/ctf_class/blob/master/crypto/nuclear_bomb_red/bomb?raw=true)

## Initial Analysis 
For this challenge, we were given a binary file [bomb](https://github.com/kkatayama/ctf_class/blob/master/crypto/nuclear_bomb_red/bomb?raw=true).

![intro.png](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/nuclear_bomb_red/intro.png)

This time we need to enter the `Clock Resynchronization Sequence`.

## Tools 
* radare2 (bash)
* cutter (osx GUI for radare2)

## Computing the Answer 
### Debugging

![verify](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_red/verify.png)

This problem had a lot going on so I set breakpoints everywhere and realized that this thing recomputes itself a number of times.  First, the `AND` with `0x1f` set the right 5 bits.  
Then some right and left shifting, increment ++, and repeat while checking when `not var` or rather `var == 0`.



## The Flag 
```ObjectScript
UDCTF{youwillneverguessthis}
```
