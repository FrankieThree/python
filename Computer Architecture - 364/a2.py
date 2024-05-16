# Assignment 2 - CORRECT

from bcpu import *

# homework 
Set(r1, 0b1111_1100) 
# set r3 to 0000 0000 1111 0000 
# using mask And 
# set r4 to 0000 0000 1101 1100 
# using mask And

# set r3
Set(r2, 0b0000_1100)
Not(r2, r2)
And(r3, r2, r1)
printrb(r3)

# set r4
Set(r2, 0b0010_0000)
Not(r2, r2)
And(r4, r2, r1)
printrb(r4)
