# Assignment 9 - CORRECT
# Define Multiply for two number
# r4 = r2 * r3
# where r2 and r3 are positive numbers
from bcpu import *

# python version
# input
p2 = 2
p3 = 3 # counter
# output
# p4
p4 = 0

while p3>0:
    p4 = p4 + p2
    p3 = p3-1
    
print(p4)


# assembly class solution
# p4= p2 * p3
mul = """

Set(r4, 0)
#>while p3>0:
# if p3<= 0: goto endwhile
Addi(ar, pc, ?endwhile)
Set(r9, 0)
Sub(r9, r9, r3)
Movep(pc, ar, r9) # need a positive number, compare 0 - p3 >= 0
    # inside while loop
    Add(r4, r4, r2) # p4 = p4 + p2
    Subi(r3, r3, 1) # p3 = p3 - 1
    Subi(pc, pc,?while)
#>endwhile

"""

# testing code
# include testing code inside this handle
if __name__ == "__main__":
    # input p2 and p3 are positive numbers
    Set(r2, 22) #p2 = 2
    Set(r3, 3) #p3 = 3 #counter

    start(mul)

    # output p4
    Move(r4, r4) 
