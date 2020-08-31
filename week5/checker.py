def main():
    name = input("ur name: ")
    checker(name)


def checker(name):
    finished = False
    result = 0
    while not finished:
        try:
            # TODO: this line
            # TODO: this line
            result = int(name)
            finished = True
        except ValueError:  # TODO - add something after except
            print("Please enter a valid integer.")
    print("Valid result is:", result)


main()
