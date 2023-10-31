import serial
import sys

import os

out = sys.stdout

sentence_len = 18

s = serial.Serial("/dev/ttyUSB0", 2400)
print (f"baud = {s.baudrate}")
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
        out.write("timout\n")
    # read rest of sentence, discard it. 
    bs = s.read(sentence_len-1)
    if len(bs) != sentence_len -1 :
        # uh, something went wrong, resync.
        continue 
    while True:
        bs = s.read(18)
        # check
        if len(bs) != 18:
            break
        if len(bs) == 18 and bs[0] < 128:
            break
        out.write(", ".join([str(b) for b in bs]))
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


