# sorry ducky
import os
file = open("emojis.txt", "w")
string = ""
#for i in range(100):
stream = os.popen("nc ctf.cs.technion.ac.il 4001")
string += stream.read()
stream.close()
print(string)
