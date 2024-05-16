# Norman Cook
# 01/24/21

# Assignment
# use previous div and mod assignment
# but this one can handle division by 0
# Div by 0
from bcpu import *

# what happens when the denominator is zero for division

# python version
# input
p2 = 20
p3 = 5

# init
p4 = 0
p5 = 0

# make a case to handle 0
if p3 != 0:
    while p2 >- p3:
        p2 = p2 - p3
        p4 = p4 + 1
    p5 = p2

# output
print(p4)
print(p5)

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
