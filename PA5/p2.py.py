def method(integer):
    for operations in range(1, 201):
        if (integer % 2 == 0):
            integer /= 2
        elif (integer % 2 != 0):
            integer = (integer * 3) + 1

        if (integer == 1):
            print("Final value", int(integer), "number of operations performed", operations)
            return()
        print("Next value is: ", int(integer))



def main():
    init = int(input("Initial value is: "))
    method(init)
main()
