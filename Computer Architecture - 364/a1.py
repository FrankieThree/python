# Assignment 1 - CORRECT
# r14 = -1400
from bcpu import *

Set(r0, 0)
Set(r14, 1400%256)
Seth(r14, 1400//256)
Sub(r14, r0, r14)
printr(r14)
