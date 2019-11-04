def art():
	j = 11
	for i in range(6):
		for x in range(i):
			print("\\\\", end="")
		
		for y in range(j):
			print("!!", end="")

		for z in range(i):
			print("//", end="")
		j = j-2
		print()

art()
