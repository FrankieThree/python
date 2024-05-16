# Vigenere Cipher A02
# Python 3.8
# Frankie
import sys
import string

# constants
# Some Ideas borrowed form: https://inventwithpython.com/bigbookpython/project61.html
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# main loop of program
def Main(mode='-e', key=''):

    while(1):
        # retrieve std input
        try:
            message = input()
        # EOF: End of File Error
        except EOFError:
            return

        # encrypt message
        stdout = ''
        keyLen = len(key)
        messLen = len(message)
        #pIdx = 0
        keyIdx = 0
        kIdx = 0
        keyChar = ''
        
        for messIdx in range(0, messLen):
            # check case key length equals 0
            if keyLen!=0:
                keyChar = key[keyIdx % keyLen]
            else:
                keyChar = key[0]

            # message character and alphabet index of character
            messChar = message[messIdx]
            pIdx = AlphabetIndex(messChar)
            
            # if key character is in alphabet, then update key index
            while not InAlphabet(keyChar):
                keyIdx += 1
                keyChar = key[keyIdx % keyLen]
            kIdx = AlphabetIndex(keyChar)
            alphabetLen = 26

            # check if character is part of alphabet
            if not InAlphabet(messChar):
                stdout += messChar
            else:

                # check case
                if messChar.isupper():
                    # check to encode or decode
                    if (mode == '-e'):
                        rotIdx = (pIdx + kIdx) % alphabetLen
                    else:
                        rotIdx = (26 + pIdx - kIdx) % alphabetLen # fix division by 0
                    stdout += UPPER_LETTERS[rotIdx]
                    
                elif messChar.islower():
                    # check to encode or decode
                    if (mode == '-e'):
                        rotIdx = (pIdx + kIdx) % alphabetLen
                    else:
                        rotIdx = (26 + pIdx - kIdx) % alphabetLen
                    stdout += LOWER_LETTERS[rotIdx]

                # increase key index
                keyIdx += 1
                
        print(stdout)

# rotation: character's index in alphabet
def AlphabetIndex(char):
    if char.isupper():
        return string.ascii_uppercase.index(char)
    elif char.islower():
        return string.ascii_lowercase.index(char)

# checks if character is a-z or A-Z
def InAlphabet(char):
    return char.isupper() or char.islower()

# python saves arguments passed in from command line
# access sys package for these arguments
mode = sys.argv[1]
if (mode != '-e' and mode != '-d'):
    print('Incorrect Mode: Using '+mode+'\nTry [-e] or [-d]', file=sys.stderr)
    sys.exit()
    
try:
    key = sys.argv[2]
except:
    print('No Key Set', file=sys.stderr)
    key = ''

Main(mode, key)





















    
