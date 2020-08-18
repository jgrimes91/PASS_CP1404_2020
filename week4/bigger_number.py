def main():
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter another number: "))

    largest_number(num_one, num_two)


def largest_number(num_one, num_two):
    if num_one > num_two:
        print("{} is bigger than {}".format(num_one, num_two))
    else:
        print("{} is bigger than {}".format(num_two, num_one))


main()
