def prompt():
    itera = int(input("How many numbers do you want to enter?"))
    print(calc(itera))
   # numbs = calc(itera)
  #  print(numbs)


def calc(iterations):
    biggest = 0
    smallest = 0
    for i in range(1, iterations + 1):
        n = input("Number:")
        n = int(n)
        if n > biggest:
            n = biggest
        elif n < smallest:
            n = smallest
    biggest = "Largest =", biggest
    smallest = "Smallest =", smallest
    return(biggest, smallest)

prompt()

