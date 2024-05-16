# Steg
# Python 3.8
# Frankie - 10/23/23
# Terminal Command
# python3 steg.py -s -B -o1024 -i256 -wsb.bmp -hsB.bmp > output.file
import sys
import math

# sentinel is a byte array
SENTINEL = [0x0,0xff,0x0,0x0,0xff,0x0]

# initiate steganography
# a : action to perform (store or retrieve)
# m : mode (bit or byte)
# o : offset
# i : interval
# w : wrapper file
# h : hidden file
def steg(a, m, o, i, w, h):
    if (a=='s'):
        if (m=='b'):
            storeBit(w, h, o, i)
        elif (m=='B'):
            storeByte(w, h, o, i)
    elif (a=='r'):
        if (m=='b'):
            retrieveBit(w, o, i)
        elif (m=='B'):
            retrieveByte(w, o, i)
    else:
        print('ERR WRONG INPUT! Try -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]')
    
def storeByte(w, h, offset, interval):  
    # rb : read binary mode
    wrapper_file = open(w, 'rb')
    hidden_file = open(h, 'rb')

    # byte arrays
    wrapper_byte_array = bytearray(wrapper_file.read())
    hidden_byte_array = bytearray(hidden_file.read())

    i=0
    while(i < len(hidden_byte_array)):
        wrapper_byte_array[offset] = hidden_byte_array[i]
        
        offset += interval
        i += 1

    i=0
    while(i < len(sentinel)):
        wrapper_byte_array[offset] = sentinel[i]
        
        offset += interval
        i += 1

    # output
    sys.stdout.buffer.write(bytearray(wrapper_byte_array))
    wrapper_file.close()
    hidden_file.close()
        
def storeBit(w, h, offset, interval):
    # rb : read binary mode
    # wb : write binary mode
    wrapper_file = open(w, 'rb')
    hidden_file = open(h, 'rb')
    
    # byte array
    wrapper_byte_array = bytearray(wrapper_file.read())
    hidden_byte_array = bytearray(hidden_file.read())

    i=0
    while(i < len(hidden_byte_array)):
        # lsb: least significant bit of current byte
        for j in range(8):
            #print(j)
            if offset >= len(hidden_byte_array):
                break

            # grab current msb
            msb = hidden_byte_array[i] & (1 << 7-j)
            msb_shift = msb >> (7-j)

            # store msb in lsb place
            wrapper_byte_array[offset] &= 0b1111110
            wrapper_byte_array[offset] |= (msb_shift)
            
            # increment offset
            offset += interval

        # save new lsb byte (1/8 msb data)
        i+=1
        
    i=0
    while(i < len(sentinel)):
        # lsb: least significant bit of current byte
        for j in range(8):
            if offset >= len(sentinel):
                break

            # grab current msb
            msb = sentinel[i] & (1 << 7-j)
            msb_shift = msb >> (7-j)
            
            # store msb in lsb place
            wrapper_byte_array[offset] &= 0b1111110
            wrapper_byte_array[offset] |= (msb_shift)

            # increment offset
            offset += interval

        # save new lsb byte (1/8 msb data)
        i+=1
        
    # output
    sys.stdout.buffer.write(bytearray(wrapper_byte_array))
    wrapper_file.close()
    hidden_file.close()

def retrieveByte(w, offset, interval):
    # rb : read binary mode
    wrapper_file = open(w, 'rb')
    hidden = []
    hidden_sentinel = []
    sentinel_count = 0

    # byte array
    wrapper_byte_array = bytearray(wrapper_file.read())
    
    while(offset < len(wrapper_byte_array)):
        # current byte
        b = wrapper_byte_array[offset]

        # check if byte matches sentinel
        if b == sentinel[sentinel_count]:
            # save byte, update sentinel index
            hidden_sentinel.append(b)
            sentinel_count += 1
        else:
            # if hidden sentinel is full, then store values and reset
            if len(hidden_sentinel) > 0:
                #print(len(hidden_sentinel))
                hidden_sentinel.reverse()
                for byte in hidden_sentinel:
                    hidden.append(byte)
                sentinel_count = 0
                hidden_sentinel = []

            # save current byte to final file
            hidden.append(b)

        # check sentinels
        if hidden_sentinel == sentinel:
            break
        offset += interval

    # output
    sys.stdout.buffer.write(bytearray(hidden))
    wrapper_file.close()

def retrieveBit(w, offset, interval):
    # rb : read binary mode
    wrapper_file = open(w, 'rb')
    hidden = []
    hidden_sentinel = []
    sentinel_count = 0

    # byte array
    wrapper_byte_array = bytearray(wrapper_file.read())
    
    while(offset < len(wrapper_byte_array)):
        # current bit
        wrapper_byte = wrapper_byte_array[offset]
        lsb_shift = 0
        
        # lsb: least significant bit of current byte
        for j in range(8):
            if offset >= len(wrapper_byte_array):
                break
            
            # grab lsb
            lsb = wrapper_byte_array[offset] & 1
            lsb_shift = lsb_shift ^ (lsb << 7-j) # 7-j # this might have to be reversed?

            # increment offset
            offset += interval

        byte = lsb_shift
        
        # check if byte matches sentinel
        if byte == sentinel[sentinel_count]:
            # save byte, update sentinel index
            hidden_sentinel.append(byte)
            sentinel_count += 1
        else:
            # if hidden sentinel is full, then store values and reset
            if len(hidden_sentinel) > 0:
                #print(len(hidden_sentinel))
                hidden_sentinel.reverse()
                for byte_hs in hidden_sentinel:
                    hidden.append(byte_hs)
                sentinel_count = 0
                hidden_sentinel = []

            # save current byte to final file
            hidden.append(byte)

        # check sentinels
        if hidden_sentinel == sentinel:
            break

    # output
    #print(hidden)
    sys.stdout.buffer.write(bytearray(hidden))
    wrapper_file.close()

#TAKE IN PARAMETERS
action = sys.argv[1][1]
mode = sys.argv[2][1]

#checks for offset, interval, hidden, and wrapper then strips and stores them into variables
# interval: interval to be repeated in bits
# offset: offset for start in bits
# w: wrapper
# h: hidden
#try:
for check in sys.argv:
    if('-o' in check):
        try:
            offset = int(check.replace('-o',''))
        except:
            print('off')
            offset = 0
    if('-i' in check):
        try:
            interval = int(check.replace('-i',''))
        except:
            interval = 1
    if('-w' in check):
        w = check.replace('-w','')
    if('-h' in check):
        h = check.replace('-h','')
        
steg(action, mode, offset, interval, w, h)
#except:
#    print('Not Enough Inputs! Try -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]')
    








