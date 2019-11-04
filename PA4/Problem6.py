def art2():
	c = 4
	j = (c * 2) - 1
	for i in range(c):
		for x in range(i):
			print("\\\\", end="")
		
		for y in range(j):
			print("!!", end="")

		for z in range(i):
			print("//", end="")
		j = j-2
		print()

art2()