### ASSIGNMENT 16 ###
# Update the div asm program to be able to handle
# positive and negative and zero numbers. (if d/0, r4=0, r5=0)
# div(r2, r3) -> (r4, r5):
# make it a divolib file
# and create a main file to provide number for testing
from bcpu import *
import a16-div0

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
