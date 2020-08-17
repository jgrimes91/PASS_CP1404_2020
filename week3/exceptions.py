valid_input = False
while not valid_input:
    try:
        numerator = int(input("Numerator: "))
        denominator = int((input("Denominator: ")))
        fraction = numerator/denominator
        valid_input = True
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero, try again")

print("Fraction result is {}".format(fraction))
