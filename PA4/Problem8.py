def exp():
	base = int(input("Please enter an integer indicating the base:"))
	exp = int(input("Please enter a positive integer indicating the exponent:"))
	for i in range(exp+1):
		num = 1
		for x in range(1,i+1):
			num = base * num
		print(num, " ", end="")

exp()
