# Processor.txt v1.0.1 Specs
Not yet implemented, due to difficulties with making the loops. Please help by making a pull request on branch v1.1

## Usage

python3 processor.txt.py \[options\]

## Registers:

a  
b  
c  
d  
e  
f  
g  
h  

## Instructions:

! => Logical NOT of DATA, writes to DATA  
& => Logical AND between selected register and DATA, writes to DATA  
^ => Logical XOR between selected register and DATA, writes to DATA  
, => Copy DATA to a (selects a)  
$ => Pops a to DATA (doesn't erase a)  
. => Copy DATA to b (selects b)  
\* => Pops b to DATA (does erase b)  
/ => Copy DATA to c (selects c)  
? => Pops c to DATA (does erase c)  
; => Copy DATA to d (selects d)  
: => Pops d to DATA (does erase d)  
@ => Copy DATA to e (selects e)  
\# => Pops e to DATA (does erase e) 
\[ => Copy DATA to f (selects f)  
{ => Pops f to DATA (does erase f)  
\] => Copy DATA to g (selects g)  
} => Pops g to DATA (does erase g)  
\ => Copy DATA to h (selects h)  
| => Pops h to DATA (does erase h)  
\> => Moves DATA to the RIGHT  
< => Moves DATA to the LEFT  
\+ => Increment DATA, mod 256  
\- => Decrement DATA, mod 256  
~ => Print DATA to STDOUT  
% => bitshift DATA right  
_ => bitshift DATA left, mod 256  
\` => nop  

## Other stuff
DATA is the data pointer, CODE is the code pointer (that always moves forward in v1.0)

Comments are any data after the first line of the program, as the 
interpreter only reads the first line.


The processor is big-endian, because that was the easiest way to implement the PTVM
## Options

  -c:
    Has code be submittied on the command line, rather than in code.pt
  -a:
    Makes ~ output ASCII rather than numbers.
  -d or --debug:
    Perform a debug memory dump at the end of execution.

# Plea For Help
If you can help make loops work, please do so. Make a pull request for the v1.1 branch.
