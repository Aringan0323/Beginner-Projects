def header():
	print("Year     ", end="")
	print("Curr Balance    ", end="")
	print("Interest        ", end="")
	print("New Deposit      ", end="")
	print("New Balance")


	
def prompt():
	years = int(input("For how many years do you want to save?"))
	print("Year     ", end="")
	print("Curr Balance    ", end="")
	print("Interest        ", end="")
	print("New Deposit      ", end="")
	print("New Balance")
	return(years)


def calc():
	
	
	balance = 1000
	interest = 0.0065
	for i in range(prompt()):
		print(i, "\t", end="")
		print('%.2f' % balance, "\t", end="")
		balance = balance + (balance * interest) + 100
		print('%.2f' % ((interest * 100)), "\t\t", end="")
		print(100.0, "\t\t", end="")
		print('%.2f' % balance, end="")
		interest = interest + (interest * interest)
		print()


calc()