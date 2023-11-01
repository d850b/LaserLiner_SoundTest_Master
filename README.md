# LaserLiner SoundTest-Master

Protocol and Programs for Laserliner SoundTest-Master device, bought ~2012 from Conrad (rev 0111)

It has a serial interface (led output) 2400 baud, 8, N, 1

It has "binary" output. Each "sentence" consists of 18 bytes, the first one is >127 (sync).

My current guesswork amounts to this:

| idx | value      | remark |
|-----|------------|--------|
| 0   | Start and Status | >127
| 1   | Over/Under range
| 2   | db 100     
| 3   | db 10
| 4   | db 1
| 5   | db 0.1
| 6   | ??         | 0
| 7   | ??         | 0
| 8   | ??         | 0
| 9   | ??         | 1
|10   | ??         | 0
|11   | ??         | 1
|12   | HH 10
|13   | HH 1
|14   | MI 10
|15   | MI 1
|16   | SS 10 
|17   | SS 1


Example readout: (first line is 33.3 db at 00:04:03)
```
   160    40     0     3     3     3     0     0     0     1     0     1     0     0     0     4     0     3
   160    40     0     3     3     3     0     0     0     1     0     1     0     0     0     4     0     4
   160    40     0     3     4     7     0     0     0     1     0     1     0     0     0     4     0     5
   160     8     0     3     3     4     0     0     0     1     0     1     0     0     0     4     0     6
   160     8     0     3     3     3     0     0     0     1     0     1     0     0     0     4     0     7
   160     8     0     3     3     4     0     0     0     1     0     1     0     0     0     4     0     8
   160     8     0     3     3     5     0     0     0     1     0     1     0     0     0     4     0     9
   160     8     0     3     3     3     0     0     0     1     0     1     0     0     0     4     1     0
   160     8     0     3     3     3     0     0     0     1     0     1     0     0     0     4     1     1


```