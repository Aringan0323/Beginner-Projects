def printnbr():
	num = int(input("Please enter a positive integer:"))
	for i in range(1, num+1):
		print("[", i, "] ", end="")
printnbr()