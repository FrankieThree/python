# TimeLock Algorithm
# Python 3.8
# Frankie ~ 10/11/23
# Terminal Call
# echo "1999 12 31 23 59 59" | python timelock.py
import sys
import datetime
import hashlib
from datetime import datetime
from dateutil.tz import gettz

MANUALTIME = False
#SYSTIMEIN = '2017 03 23 18 02 06'
#SYSTIMEIN = '2023 01 01 00 00 00'

# check if character is letter
def isCharLetter(c):
    asci = ord(c)
    if (97 <= asci <= 102 or 65 <= asci <= 70):
        return True
    return False

# check if character is number
def isCharNumber(c):
    asci = ord(c)
    if (48 <= asci <= 57):
        return True
    return False

# extract the first two letters from right-to-left
# extract the first two numbers from left-to-right
# KEEP ORDER ON REVERSE?
def extracteCodeFromHash(h):
    code = ''
    count = 0
    for char in h:
        if isCharLetter(char):
            code += char
            count += 1
        if count >= 2:
            break

    count = 0
    for char in h[::-1]:
        if isCharNumber(char):
            code += char
            count += 1
        if count >= 2:
            break
    return code

def main(epoch):
    # read the epoch time from stdin
    # string format : YYYY MM DD HH mm SS
    epochTimeStr = epoch
    eLst = [ int(a) for a in epochTimeStr.split() ]
    epochTime = datetime(eLst[0],eLst[1],eLst[2],eLst[3],eLst[4],eLst[5])

    # read the current system time
    # string format : YYYY MM DD HH mm SS
    if MANUALTIME:
        sysTimeStr = SYSTIMEIN
        sLst = [ int(a) for a in sysTimeStr.split() ]
        sysTime = datetime(sLst[0],sLst[1],sLst[2],sLst[3],sLst[4],sLst[5])
    else:
        sysTime = datetime.now()
        sysTimeStr = sysTime.strftime("%Y %m %d %H %M %S")

    # activate time zones and DST aware times
    tZone = gettz('US/Eastern')
    epochTime, sysTime = epochTime.replace(tzinfo=tZone), sysTime.replace(tzinfo=tZone)
    utcdelta = epochTime.utcoffset() - sysTime.utcoffset()

    # elapsed time
    interval = 60
    elapsed = int((sysTime - epochTime + utcdelta).total_seconds())
    elapsed = elapsed - elapsed % interval

    # hash
    h1 = hashlib.md5(str(elapsed).encode()).hexdigest()
    result = hashlib.md5(h1.encode()).hexdigest()

    sys.stdout.write('Epoch Time: '+epochTimeStr+
                     'System Time: '+result+"\n"+
                     extracteCodeFromHash(result)+"\n"+result[len(result)/2]+"\n")

# read stdinput
try:
    # sanitize input
    date = sys.stdin.read()
    #fileBin = file
    main(date)
except:
    print('File Does Not Exist', file=sys.stderr)
