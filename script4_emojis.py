while True:
	s = input("Input string\n")
	known_letters={'🤘': ' ', '🐲': 'a', '🕹': 'b', '✨': 'c', '😃': 'd', 
	'🤖': 'e', '🎵': 'f', '🍝': 'g', '😎': 'h',
                '💪': 'i', '🙂': 'j', '🐂': 'k', '🎱': 'l', '👿': 'm', '🌺': 'n', '👏': 'o', 
                '📽': 'p', '🍃': 'q',
                '🐵': 'r', '👶': 's', '🍕': 't', '🆕': 'u', '🖐': 'v', '😪': 'w', '😶': 'x', '🚩': 'y', '😞': 'z', '👀': '!'}

	res = dict((v,k) for k,v in known_letters.items())

	for char in s:
		if char in known_letters:
			print(known_letters[char].upper(),end="")
		elif char in res:
			print(res[char], end="")
		else:
			print(char, end="")
	print("")
