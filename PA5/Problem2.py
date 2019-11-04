def algorithm(n):
	counter = 0
	val = n
	for i in range(1000):
		
		if ((val % 2) == 0) and (val != 1):
			val =  (val / 2)
		elif ((val % 2) == 1) and (val != 1):
			val = (val * 3) + 1

		if val == 1:
			print("Final value 1, number of operations performed ", i)
			return()
		
		print("Next value is: ", val)


def main():
	number = int(input("Initial value is:"))
	algorithm(number)

main()


