f = open("data.txt", "r")
data = f.read()
txt = data.split("\n")
list = []
for line in txt:
	for word in line.split("🤘"):
		list.append(word)
string_out = ""
for word in sorted(list, key=len):
	string_out += word + "\n"
f.close()
f = open("out.txt", "w")
f.write(string_out)
