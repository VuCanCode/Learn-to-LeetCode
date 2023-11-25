def main():
    digits = input()
    number = digits.split(" ")
    digit1 = int(number[0])
    digit2 = int(number[1])
    summation = digit1 + digit2
    print(summation)

if __name__ == "__main__":
    main()