import ast # asat? :P
file = open("output.txt", "r")
dict = ast.literal_eval(file.read())
file = open("output_intersections.txt", "w")
file.write(str(dict.keys()))
