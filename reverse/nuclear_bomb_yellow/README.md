# Nuclear_Bomb_Yellow

You must defuse Dr. Von Noizeman's nuclear bomb!
<p>The flag for this challenge is the answer for the <font color="yellow"><b>yellow</b></font> wire, wrapped in the <b>UDCTF{}</b> flag format.</p>

FILE: [bomb](https://github.com/kkatayama/ctf_class/blob/master/reverse/nuclear_bomb_yellow/bomb?raw=true)

## Initial Analysis 
For this challenge, we were given a binary file [bomb](https://github.com/kkatayama/ctf_class/blob/master/reverse/nuclear_bomb_yellow/bomb?raw=true).

When we run the binary, we are greeted with a menu selection: `[1] YELLOW [2] GREEN [3] BLUE [4] RED`.
Selecting `[1]` prompts us to `ENTER UNLOCK PASSWORD 1:`

![intro.png](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_yellow/intro.png)


## Tools 
* radare2 (bash)
* cutter (osx GUI for radare2)

## Computing the Answer 
### Debugging

![verify](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_yellow/verify.png)

Looking at the debugger, after we enter the password the binary checks each 4-byte integer that was submitted.  To make sure of this, I entered what I expected the checked values to be, ran it, and set some breakpoints just before the final check before being cleared.  However, after the final check of the password entered, two adjustments are made before it is considered a valid code to `Disengage` the yellow wire.  This is a subtle but very important to recognize as this became challenging with other wires. 

### RESULTS
![hack](https://raw.githubusercontent.com/kkatayama/ctf_class/master/reverse/nuclear_bomb_yellow/hack.png)

## The Flag 
```ObjectScript
UDCTF{84371065}
```
