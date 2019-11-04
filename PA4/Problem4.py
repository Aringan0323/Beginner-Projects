def fun3():
	v = 4
	for i in range(1,6):
		for x in range(v):
			print("  ", end="")
		v = (v-1)
		for y in range(i):
			print("* ", end="")
		print()
fun3()

