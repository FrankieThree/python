### Assignment ###
# using previous homework
# multiplication for positve or negative numbers
# p4 = p2 * p3
#input p2 and p3 are positive or negative numbers

# python version
p2 = -2
p3 = 3 # COUNTER
# output
# p4

# fix sign
# the counter needs to be positive
if p3 < 0:
    p3 = -p3
    p2 = -p2
# mul
p4 = 0
while p3>0:
    p4 = p4 + p2    # add a negative number repeatedly if p2 is negative
    p3 = p3 - 1

print(p4)

mul = """
# p4 = p2 * p3, where p2 and p3 can be negative

# fix sign
# if p3 < 0:
# if p3 >= 0: goto endif
Addi(ar, pc, ?endif)
Movep(pc, ar, r3)
    # then part
    Not(r3, r3) # p3 = -p3
    Addi(r3, r3, 1) # p2 = -p2
    Not(r2, r2) # p2 = -p2
    Addi(r2, r2, 1)
#>endif

# same code from previous assignment
Set(r4, 0) # p4 = 0
#>while p3>0:
Addi(ar, pc, ?endwhile)
Set(r9, 0)
Sub(r9, r9, r3)
Movep(pc, ar, r9)
    Add(r4, r4, r2) #p4 = p4 + p2
    Subi(r3, r3, 1) #p3 = p3 - 1
    Subi(pc, pc,?while)
#>endwhile

"""

# testing
if __name__ == "__main__":
    # input p2 and p3 are positive numbers
    Set(r2, 22) #p2 = -22
    Not(r2, r2)
    Addi(r2, r2, 1)
    Set(r3, 3)  #p3 = 3
    Not(r3, r3)
    Addi(r3, r3, 1)

    start(mul)

    #output
    #p4
    Move(r4, r4)
