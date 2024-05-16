# assignment 8 - CORRECT
# 14/01/21
from bcpu import *

### QUIZ ###
# if then else p2<=p3

# python version
p2 = 2
p3 = 3

if p2<=p3:
    p4 = 4
    p5 = 5
else:
    p4 = -4
    p5 = -5

print(p4)
print(p5)

# CLASS SOLUTION
quizfile = """
Set(r2, 31) #p2 = 2
Set(r3, 3) #p3 = 3

#if p2<=p3:
# goto else if not true: p2>p3
Addi(ar, pc, ?else)
Sub(r9, r3, r2)   # r9 = p3 - p2, which is negative, p2 > p3
Moven(pc, ar, r9) # moven requires a negative number, r9
    # then part
    Set(r4, 4) #p4 = 4
    Set(r5, 5) #p5 = 5
    Addi(pc, pc, ?endif) # goto endif
#>else:
    Set(r4, 4) # p4 = -4
    Not(r4, r4)
    Addi(r4, r4, 1)
    Set(r5, 5) # p5 = -5
    Not(r5, r5)
    Addi(r5, r5, 1)
#>endif
Move(r4, r4) # print(p4)
Move(r5, r5) # print(p5)

"""

start(quizfile)
