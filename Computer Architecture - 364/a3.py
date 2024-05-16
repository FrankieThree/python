# Assignment 3 - CORRECT
# Stack Push and Pop
from bcpu import *

# push 44
# push 55
# pop into r5

Set(r1, 44)
Addi(st, st, 1)
Store(st, r1)

Set(r1, 55)
Addi(st, st, 1)
Store(st, r1)

Load(r5, st)
Subi(st, st, 1)

printd(0,10)
printr(r5)
