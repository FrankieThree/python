# XOR Crypto
# Python 3.8
# Frankie - 10/15/23
# ENCRYPT: python xor.py < ciphertext > outputtext
# DECRYPT: python xor.py < ciphertext
import sys

KEY = 'key' #'key2'

# set up byte arrays
inputBA = bytearray(sys.stdin.buffer.read())
keyFile = open(KEY, 'rb')
keyBA = bytearray(keyFile.read())

result = bytearray(b'00000000')
bits = []

# cycle through key byte array
for i in range(0,len(inputBA)):
    k = keyBA[i%len(keyBA)]
    n = inputBA[i]
    bits.append(k ^ n)

# outpu
sys.stdout.buffer.write(bytearray(bits))
