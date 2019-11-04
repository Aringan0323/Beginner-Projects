
def romNum(number):
    count = 0
    for i in number:
        count += 1
        if (count == len(number) - 3):
            print("M" * int(i), end="")
        elif (count == len(number) - 2):
            if (1 <= int(i) <= 3):
                print("C" * int(i), end="")
            elif (int(i) == 4):
                print("CD", end="")
            elif (5 <= int(i) <= 8):
                print("D" + ((int(i) - 5) * "C"), end="")
            elif (int(i) == 9):
                print("CM", end="")
        elif (count == len(number) - 1):
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
    print("Enter a number to convert to Roman Numerals")
    num = input()
    print()
    romNum(num)
main()
