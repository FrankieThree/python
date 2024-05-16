# ftp covert message
# Python 3.8
# Frankie - 10/12/23
import socket
from sys import stdout
from time import time
import math

# enables debugging output
DEBUG = False

# set the server's IP address and port
#ip = '138.47.99.64'
#ip = 'localhost'
#port = 31337
#port = 1334
ip = 
port = 

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# variables
data = s.recv(4096).decode()
offset = 0.05
timesL = []
timesH = []
binMess = ''
binMessCopy = ''
lowAvg = 0
highAvg = 100
firstPassL = True
firstPassH = True
message = ''

# check a list for argument
def doesContain(l, a):
    for i in l:
        if i == a:
            return True
    return False

# convert 8-bit Binary into ascii
# byte : string representation of 8-bits
def decodeBin8(byte):
    if len(byte)<8:
        print('error in byte length')
        return '?'
    if int(byte, 2)>127:
        return '!'
    # convert byte to character
    return chr(int(byte, 2))

# save message values
# c : single character
def saveBinMessage(c):
    global binMess
    global binMessCopy
    
    binMess += c
    binMessCopy += c
    
# save the given delta value
# d : time taken to retrieve a message character
def saveDelta(d):
    global lowAvg
    global highAvg
    global firstPassL
    global firstPassH


    # save d to either first or second
    checkL = abs(d - lowAvg)
    checkH = abs(d - highAvg)

    # offset is a decimal ex. 0.50 == 50%
    if checkL <= lowAvg * (offset+1) or firstPassL:
        firstPassL = False
        timesL.append(d)
        # update average
        lowAvg = sum(timesL) / len(timesL)
        # update message
        saveBinMessage('0')
    elif checkH <= highAvg * (offset+1) or firstPassH:
        firstPassH = False
        timesH.append(d)
        # update average
        highAvg = sum(timesH) / len(timesH)
        # update message
        saveBinMessage('1')
    else:
        # questionable ?
        saveBinMessage('?')

# read in messages from server until EOF
while data.rstrip('\n') != 'EOF':

    # output the data
    stdout.write(data)
    stdout.flush()

    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    saveDelta(delta)

    # check for a bytes worth of information
    if len(binMessCopy)%8==0:
        # convert byte to ascii
        byte = binMessCopy[:8]
        binMessCopy = ''
        char = decodeBin8(byte)
        message += str(char)

    # check if EOF
    if message[-3:]=='EOF':
        print('Exit: EOF Found')
        break

    # write to stdout is faster than print
    if DEBUG:
        stdout.write(' {}\n'.format(delta))
        stdout.flush()

#print('Binary: '+binMess)
print('Message: '+message)

invBinMess = ''
invert = input('Invert Binary? [y/n] : ')
if invert == 'y':
        for bit in binMess:
            if bit == '0':
                invBinMess += '1'
            elif bit == '1':
                invBinMess += '0'
            else:
                invBinMess += '?'

        byteLen = 8
        numOfBytes = math.floor(len(invBinMess)/byteLen)

        invMessage = ''
        for n in range(0,numOfBytes):
            byte = invBinMess[0+n*byteLen:byteLen+n*byteLen]
            if doesContain(byte, '?'):
                char = '?'
            else:
                char = decodeBin8(byte)
            invMessage += char

        #print('Inverted Binary: '+invBinMess)
        print('Inverted Message: '+invMessage)

# close the connection to the server
s.close()
