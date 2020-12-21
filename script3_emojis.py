for i in range(0, 13):
	f = open("emojis_len"+str(i), "r")
	lines = f.read().split("\n")
	result = list(set(sorted(lines, key = lines.count, reverse = True)))
	file = open("emojis_by_freq"+str(i), "a")
	for word in result:
		file.write(word + "\n")
