def main():
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter another number: "))

    largest_number(num_one, num_two)


def largest_number(num_one, num_two):
    if num_one < num_two:
        biggest_num = num_two
        smallest_num = num_one
    else:
        biggest_num = num_one
        smallest_num = num_two
    print("{} is bigger than {}".format(biggest_num, smallest_num))


main()
