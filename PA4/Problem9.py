def chart(min, max):
	strt = min
	for line in range(1, max - min + 2):
		for loop1 in range(strt, max + 1):
			print(loop1, end="")
		strt += 1
		for loop2 in range(min, max - min + 1 - max):
			print(loop2, end="")
		print()












def main():
	small = int(input("Please enter a minimum integer:"))
	big = int(input("Please enter a maximum integer:"))
	chart(small, big)
main()
