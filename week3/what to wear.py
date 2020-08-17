from random import randint


def main():
    choice = randint(0, 100)
    total_dress = 0
    total_jeans = 0

    print("Helping Jess on what to wear :)")
    for i in range(0, 20):
        if choice % 2 == 1:
            print("Dress")
            total_dress += 1
        if choice % 2 == 0:
            print("Jeans")
            total_jeans += 1
        choice = randint(0, 100)

    print("Dress count: ", total_dress)
    print("Jeans count: ", total_jeans)


main()
