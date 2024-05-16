### Assignment 15 ###
# make the bitwise mul to be a mul16lib file
# create a main program to call the mul16(r2, r3)->r4
# in main r2 = 22, r3 = 33
# calling mul16
# output Mover(r4, r4)
from bcpu import *
import a15-abs

mainfile = """
#>main():
# caall function define in the same file
# from main() call funcname() def before main()
# before calling need to
    Set(r2, 22)
    Not(r2, r2)
    Addi(r2, r2, 1)
# push return addr
    Addi(ar, pc ?returnaddr) # setup relative return addr
    Addi(st, st, 1) # update stack pointer
    Store(st, ar) # push
# calling funcname()
    Set(ar, ?abs + 1) # relative to next instruction so +1
    Sub(ar, pc, ar) # upward relative addr
    Move(pc, ar)
    #>returnaddr
    Move(r3, r3)
"""

start(mainfile)
