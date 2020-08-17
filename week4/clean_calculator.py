MENU = "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit"


def main():
    print("Welcome to the Clean Calculator!")
    loop_controller = 0
    result = 0
    while loop_controller == 0:
        print(MENU)
        choice = get_valid_selection(">>> ")

        num_one = get_valid_number("Enter the first number: ")
        num_two = get_valid_number("Enter the second number: ")

        if choice == 5:
            print("Goodbye!")
            quit()
        elif choice == 1:
            result = addition(num_one, num_two)
        elif choice == 2:
            result = subtract(num_one, num_two)
        elif choice == 3:
            result = multiply(num_one, num_two)
        else:
            result = divide(num_one, num_two)
        print("The result is {}".format(result))


def get_valid_selection(prompt):
    user_errors = True
    while user_errors:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if user_input <= 0 or user_input >= 5:
                print("Choice must between between 1 and 5.")
                print(MENU)
            else:
                user_errors = False
                return user_input
        except ValueError:
            print("Whoops! Choice needs to be a number between 1 and 5. ")
            print(MENU)


def get_valid_number(prompt):
    user_errors = True
    while user_errors:
        try:
            user_input = int(input(prompt))
            user_errors = False
            return user_input
        except ValueError:
            print("Whoops! Please enter a number.")


def addition(num_one, num_two):
    return num_one + num_two


def subtract(num_one, num_two):
    return num_one - num_two


def multiply(num_one, num_two):
    return num_one * num_two


def divide(num_one, num_two):
    try:
        return num_one / num_two
    except ZeroDivisionError:
        print("Whoops cannot divide by zero")


main()
