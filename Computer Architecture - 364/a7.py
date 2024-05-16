# Norman Cook
# 01/12/2021
# abs mul3 quiz
from bcpu import *

# p3 = abs(p2) * 3
absmul3 = """

Set(r2, 5) # p2 = 5
Set(r3, 3) # p3 = 0
Not(r2, r2) # p2 = -5
Addi(r2, r2, 1)

# if p2 < 0:

# if p2 >= 0 goto endif
Set(r9, 0)
Sub(r9, r9, r2) # r9 = 0 - r2
Addi(r10, pc, ?endif) # addr of endif # this is to store
Movep(pc, r10, r2) # if r2 >= 0 goto endif (jump to endif)
    # then part
    Not(r2, r2) # p2 = ~p2
    Addi(r2, r2, 1) # p2 = p2 + 1
Movep(pc, r10, r9)
    Add(r3, r2, r2) # p3 = p2 + p2
    Add(r3, r3, r2) # p3 = p3 + p2
#>endif

Move(r2, r2) # print(p2)
"""

start(absmul3)
