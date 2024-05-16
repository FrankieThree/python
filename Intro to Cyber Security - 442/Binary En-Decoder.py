# Binary Encoder/Decoder
# Python 3.8
# Frankie
import sys

# convert byte to character
def convertByteToChar(byte):
    # base 2
    return chr(int(byte, 2))

# splice bytes from binary values
# byte length can be 8-bit or 7-bit
def spliceBinValues(fileContents, byteLength = 8):
    l = len(fileContents)
    c = byteLength
    byteValues = []
    
    while (c < l):
        # prepend for 7-bit
        if (byteLength == 7):
            byte = '0'
        else:
            byte = ''
            
        #splice
        byte += fileContents[c-byteLength:c]
        byteValues.append(byte)

        # increment
        c += byteLength
        
    return byteValues

# convert binary to ASCII characters
def Binary(fileContents):
        # check for 8 bits or 7 bits
        l = len(fileContents) - 1
        if (l % 7 == 0):
            # 7-bit input
            print('7-bit ASCII Detected')
            binValues = spliceBinValues(fileContents, 7)
            
        elif (l % 8 == 0):
            # 8-bit input
            print('8-bit ASCII Detected')
            binValues = spliceBinValues(fileContents, 8)
            
        else:
            print('Wrong Bit Count', file=sys.stderr)
        
        # convert binary to ascii
        message = ''
        for b in binValues:
            message += convertByteToChar(b)
        print(message)

# read stdinput
try:
    # sanitize input
    file = sys.stdin.read()
    fileBin = file
    Binary(fileBin)
except:
    print('File Does Not Exist', file=sys.stderr)
