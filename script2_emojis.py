file = open("words_by_freq", "r")
file_text = file.read().split("\n")
for word in file_text:
	file2 = open("words_by_freq"+str(len(word)), "a")
	file2.write(word + "\n")

