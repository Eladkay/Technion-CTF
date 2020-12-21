#!/usr/bin/python3
import hashlib, string
from pwn import *

d = {}
for c in string.printable:
	if c == '\0' or c == '\r' or c == '\n':
		continue
	d[hashlib.sha256((c+"\n").encode()).hexdigest()] = c
	d[hashlib.sha256((c+2*"\n").encode()).hexdigest()] = c
	d[hashlib.sha256((c).encode()).hexdigest()] = c


flag = ""
p = remote("ctf.cs.technion.ac.il", 4014)
p.recv()
i = 1
while True:
	p.sendline("cat ./flag.txt | sed -n 1p | cut -c {}".format(i).encode())
	try:
		r = p.recv().decode().split("\n")
		print(r)
	except:
		p = remote("ctf.cs.technion.ac.il", 4014, level='error')
		p.recv()
		continue
	finally:
		try:
			flag += d[r[0]]
		except:
			pass #flag += '?'
		finally:
			i += 1
			print(flag)
