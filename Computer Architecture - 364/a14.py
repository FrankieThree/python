### Assignment 14 ###
# mul r4 = r2 * r3
# bitwise, r2 and r3 can be positive or negative number

#-Assembly-#
mul16 = """
# fix sign
Addi(ar, pc, ?endif)
Movep(pc, ar, r2)
    Not(r2, r2)
    Addi(r2, r2, 1)
    Not(r3, r3)
    Addi(r3, r3, 1)
#>endif

# mul
Set(r4,0) # p4 = 0
Set(r1,1) # p1 = 1 # check bit, which bit is being multiplied

#>while p2 != 0:
# if p2 == 0: goto endwhile
Addi(ar, pc, ?endwhile)
Movez(pc, ar, r2)
    And(r9, r1, r2) # p9 = p1 & p2 # see the bit in p2
    Movex(r9, r3, r9) # p9 = p9 if p9 == 0 else p3 # p9 = 0 or p3
    Add(r4, r4, r9) # p4 = p4 + p9
    # update to check next bit (to the left)
    Not(r7, r1) # p7 = ~p1 # binary negation
    And(r2, r2, r7) # p2 = p2 & p7 # clear the bit that have been done
    Add(r1, r1, r1) # p1 = p1 + p1 # shift p1 << 1
    Add(r3, r3, r3) # p3 = p3 + p3 # p3 << 1
    # back up to while
    Subi(pc, pc, ?while)
#>endwhile p2 == 0
"""

Set(r2, 20)
Set(r3, 3)

start(mul16)

Move(r4, r4)
