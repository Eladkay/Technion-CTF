from bentley_ottmann.planar import segments_intersections
file = open("segments.txt","r")
text = file.read() # good luck with that
segments = []
for line in text.split("\n"):
	try:
		split_str = line.split("    ")
		x1 = float(split_str[0].split(" ")[0])
		y1 = float(split_str[0].split(" ")[1])
		x2 = float(split_str[1].split(" ")[0])
		y2 = float(split_str[1].split(" ")[1])
		segments.append(((x1, y1), (x2, y2)))
	except:
		pass
intersections = segments_intersections(segments)
file = open("output.txt","w")
file.write(str(intersections))
