#===IMPORTS===#
import socket
from sys import stdout
from time import time

#===DEBUGS===#
DEBUG_TIME = False
DEBUG_BINARY = False
DEBUG_BINLIST = False

#===GLOBALS===#
ip = "138.47.99.64"
port = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

binString1 = ''
binString2 = ''
avg = []


#===FUNCTIONS===#

def covert(nums):
    
    shift1 = 8
    l1 = []

    for i in range(0, len(nums), shift1):
        binValue = nums[i:i+shift1]
        l1.append(binValue)

    if(DEBUG_BINLIST == True):
        print(l1)
    
    
    binaryString_ASCII8(l1)
    
    
def binaryString_ASCII8(bits): #Converts Binary List into String and Returns Output
    
    result = ''
    for i in bits:
        if(len(i) != 8):
            pass
        else:
            if(int(i,2) == 8):
                result = result.rstrip(result[-1])
            else:   
                result = result+chr(int(i,2))
    
    
    
    if(result.find("EOF") != -1):
        result = result[:result.find("EOF")]
        print(result)
        print()

    else:
        print("NO MESSAGE FOUND")
        print()

def average(lst):
    return sum(lst)/len(lst)

#===MAIN===#
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()

    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    
    avg.append(delta)
   
    if (DEBUG_TIME):
        stdout.write(" {}\n".format(delta))
        stdout.flush()
    

# close the connection to the server
s.close()

check = average(avg)
print(check)

for i in range(len(avg)):
    if (avg[i] >= check):
        binString1 = binString1+'1'
        binString2 = binString2+'0'
    else:
        binString1 = binString1+'0'
        binString2 = binString2+'1'

if(DEBUG_BINARY == True):
    print("BINARY1:")
    print(binString1)
    print("BINARY2")
    print(binString2)

print("COVERT MESSAGE1:")
covert(binString1)
print("COVER MESSAGE2:")
covert(binString2)


