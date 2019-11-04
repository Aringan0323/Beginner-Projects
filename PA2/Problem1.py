#Problem 1
def main():

	i = (int(input("Enter the price of your item in cents:")))
	p = (100 - i)
	qu = (p // 25)
	di = ((p - (25 * qu)) // 10)
	ni = ((p - ((25 * qu) + (10 * di))) // 5)
	print("You bought an item for", i," cents and gave me a dollar, so your change is:")
	print(qu, "quarters")
	print(di, "dimes")
	print(ni, "nickels")

main()