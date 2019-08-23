# Nuclear_Bomb_Yellow

You must defuse Dr. Von Noizeman's nuclear bomb!
<p>The flag for this challenge is the answer for the <font color="blue"><b>blue</b></font> wire, wrapped in the <b>UDCTF{}</b> flag format.</p>

Please see the Nuclear Bomb: Yellow challenge for the bomb executable.

FILE: [bomb](https://github.com/kkatayama/ctf_class/blob/master/crypto/nuclear_bomb_blue/bomb?raw=true)

## Initial Analysis 
For this challenge, we were given a binary file [bomb](https://github.com/kkatayama/ctf_class/blob/master/crypto/nuclear_bomb_blue/bomb?raw=true).

This time we need to enter a correct sequence that satisfies a `Circuit Traversal Path`

![intro.png](https://raw.githubusercontent.com/kkatayama/ctf_class/master/crypto/nuclear_bomb_blue/intro.png)

## Tools 
* radare2 (bash)
* cutter (osx GUI for radare2)

## Computing the Answer 
### Debugging

![verify](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_blue/verify.png)

After mapping this out by hand, I realized that there are a couple different paths you can take to produce a successful `Gate Array`.  As long as the variable holding `obj.solution` and what was copied 
into `local_h` from earlier in the path, the `Gate Array` will succeed.

### RESULTS
![hack](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_blue/hack.png)


## The Flag 
```ObjectScript
UDCTF{LLRR}
```
