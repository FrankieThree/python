# FTP (Storage) Covert Channel
# Python 3.8
# ~Frankie
from ftplib import FTP

# FTP server details
#IP = "localhost"
IP = "138.47.99.64"
#DOMAIN = 'ftp.us.debian.org'
PORT = 21
USER = "anonymous"
PASSWORD = ""
#FOLDER = "/debian"
FOLDER = '/10/'
#FOLDER = '/7/'
USE_PASSIVE = True # set to False if the connection times out
METHOD = 0 # 1 = 7-bit, 0 = 10-bit

def main():
    # connect and login to the FTP server
    ftp = FTP()
    ftp.connect(IP, PORT)
    ftp.login(USER, PASSWORD)
    ftp.set_pasv(USE_PASSIVE)

    # navigate to the specified directory and list files
    ftp.cwd(FOLDER)
    files = []
    ftp.dir(files.append)

    # quit connection
    ftp.quit()

    binary = ''
    
    # display the folder contents
    for f in files:
        #print(f)

        # decode using 1 of 2 methods
        if METHOD:
            # first three permissions must be dashed '---'
            if not (isSet(f[0]) or isSet(f[1]) or isSet(f[2])):
                binary += decodePerm(f[3:10])
        elif not METHOD:
            binary += decodePerm(f[:10])

    output = decodeBin(binary)
    print(output)

# check if permission is set to anything
def isSet(c):
    if c != '-':
        return 1
    return 0

# decode permissions into binary
# all dashes '-' are 0s and anything else is 1
def decodePerm(perm):
    bin = ''
    
    # covert message
    # do i log back into ftp and grab the file?
    for c in perm:

        # convert permission set to '1' and unset (-) to '0'
        if isSet(c):
            bin += '1'
        else:
            bin += '0'

    return bin

# decode binary message
def decodeBin(bin):
    text = ''
    BITS = 7 # bit segment to decode each pass

    # cycle through binary and decode each segment
    for i in range(0, int(len(bin)/BITS)):
        # current 7 bits 
        b = bin[i*BITS:BITS+i*BITS]
        # char representation of bits
        c = chr(int(b, base=2))
        text += c

    return text

main()
