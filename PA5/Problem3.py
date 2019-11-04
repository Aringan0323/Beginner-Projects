
def convert(input):
    n = 0
    for i in number:
        n = n + 1
        if (n == len(number) - 3):
            print("M" * int(i), end="")
        elif (n == len(number) - 2):
            if (1 <= int(i) <= 3):
                print("C" * int(i), end="")
            elif (int(i) == 4):
                print("CD", end="")
            elif (5 <= int(i) <= 8):
                print("D" + ((int(i) - 5) * "C"), end="")
            elif (int(i) == 9):
                print("CM", end="")
        elif (n == len(number) - 1):
            if (1 <= int(i) <= 3):
                print("X" * int(i), end="")
            elif (int(i) == 4):
                print("XL", end="")
            elif( 5 <= int(i) <=8):
                print("L" + ((int(i) - 5) * "X"), end="")
            elif (int(i) == 9):
                print("XC", end="")
        else:
            if (1 <= int(i) <= 3):
                print("I" * int(i))
            elif (int(i) == 4):
                print("IV")
            elif (5 <= int(i) <= 8):
                print("V" + ((int(i) - 5) * "I"))
            elif (int(i) == 9):
                print("IX")
            else:
                print(" ")

def main():
    integ = input("Enter a number to convert to Roman Numerals")
    convert(integ)
main()
