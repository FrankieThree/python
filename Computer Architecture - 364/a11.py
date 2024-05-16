### Assignment ###
# division and modulus hw
# assembly program to divide and mod
# p4 = p2 // p3
# p5 = p2 % p3

# python version
# input
p2 = 20
p3 = 5

# init
p4 = 0
p5 = 0

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
# print(p4)
# print(p5)

"""

if __name__ == "__main__":
    Set(r2, 19) #p2 = 19
    Set(r3, 5) #p3 = 5

    start(div)

    Move(r4, r4)
    Move(r5, r5)
