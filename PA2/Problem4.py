#problem 4
def main():
	cookies = int(input("Please enter the amount of cookies you want to make:"))
	multiplier = (cookies / 48)
	sugar = (multiplier * 1.5)
	butter = (multiplier)
	flour = (multiplier * 2.75)
	print("You need:")
	print(sugar," cups of sugar")
	print(butter," cups of butter")
	print(flour," cups of flour")

main()
