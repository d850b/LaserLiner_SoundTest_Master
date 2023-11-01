import serial
import sys
import datetime

from enum import IntEnum

class Pos(IntEnum):
    "give positions in sentence names"
    START = 0
    STATUS = 1
    DB100 = 2
    DB10 = 3
    DB1 = 4
    DB01 = 5
    HH10 = 12
    HH1  = 13
    MI10 = 14
    MI1 = 15
    SS10 = 16
    SS1 = 17



def DecodeSentence(b:bytes):
    "sentence to string"
    db = b[Pos.DB100]*100 + b[Pos.DB10]*10 + b[Pos.DB1] + b[Pos.DB01]*0.1
    td = datetime.timedelta(
        hours =   b[Pos.HH10]*10+b[Pos.HH1], 
        minutes = b[Pos.MI10]*10+b[Pos.MI1], 
        seconds = b[Pos.SS10]*10+b[Pos.SS1])
    tds = str(td).rjust(10)
    return f"{tds};{db:6}"

out = sys.stdout
err = sys.stderr

sentence_len = 18

s = serial.Serial("/dev/ttyUSB0", 2400)
err.write (f"baud = {s.baudrate}\n")
s.timeout = 5.0

bs = bytes()

while True:
    # synchronize, i.e. read until
    # value > 127 is read.
    # the detected sentence will be discarded!
    while True:
        bs = s.read()
        if len(bs) != 0:
            if bs[0] > 127:
                break
        err.write("timout\n")
    # read rest of sentence, discard it. 
    bs = s.read(sentence_len-1)
    if len(bs) != sentence_len -1 :
        # uh, something went wrong, resync.
        continue 
    err.write("syncd\n")
    while True:
        bs = s.read(18)
        # check
        if len(bs) != 18:
            break
        if len(bs) == 18 and bs[0] < 128:
            break
        out.write(DecodeSentence(bs))
        out.write("\n")




# 2400 baud, 8, n, 1
# 1 sentence = 18 byte
#  0 = mode? and it is > 127 !!
#  1 = under/over
#  2 = db 100
#  3 = db 10 
#  4 = db 1
#  5 = db 0.1
#  6 = ?? always 0
#  7 = ?? always 0
#  8 = ?? always 0
#  9 = ?? always 1
# 10 = ?? always 0
# 11 = ?? always 1
# 12 = hr 10
# 13 = hr 1 
# 14 = mi 10
# 15 = mi 1 
# 16 = ss 10 
# 17 = ss 1


