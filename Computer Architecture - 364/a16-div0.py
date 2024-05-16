### ASSIGNMENT 16 ###
# Update the div asm program to be able to handle
# positive and negative and zero numbers. (if d/0, r4=0, r5=0)
# div(r2, r3) -> (r4, r5):
# make it a divolib file
# and create a main file to provide number for testing
from bcpu import *

div = """

# r4 = r2 // r3
# r5 = r2 % r3

# init
Set(r4, 0) #r4 = 0
Set(r5, 0) #r5 = 0

# if p3 != 0
# goto else if not true: p3 == 0
Movez(pc, ?endif, r3) 
#>while r2 >= r3:
Addi(ar, pc, ?endwhile) #address for endwhile
Set(r9, 0)
Sub(r9, r2, r3)
Moven(pc, ar, r9) # if r2 < r3 go to endwhile
    #while part
    Sub(r2, r2, r3) #r2 = r2 - r3
    Addi(r4, r4, 1) # r4 = r4 + 1
    Subi(pc, pc, ?while)
#>endwhile
Move(r5, r2) # r5 = r2

#>endif

"""

if __name__ == "__main__":
    Set(r2, 0) #p2 = 19
    Set(r3, 0) #p3 = 5

    start(div)

    Move(r4, r4)
    Move(r5, r5)
