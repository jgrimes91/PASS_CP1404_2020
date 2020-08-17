def main():
    number = number_return()
    print("Returned: ", number)


def number_return():
    try:
        number_1 = int(input("Please enter a number: "))
    except ValueError:
        print("Invalid input")
        number_1 = int(input("Please enter a number: "))
    return number_1


main()
