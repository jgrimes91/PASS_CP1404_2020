def main():
    print("Welcome to the PASS Kitchen")
    choice = input("Did you want to see the Kid's Menu? (Y)es or (N)o?").upper()
    if choice == "Y":
        kids_menu()
    else:
        quit()


def kids_menu():
    print("Kids menu: 1. Nuggets\n2. Pizza\n3. Cheeseburger\n4. Steak Sandwich\n5. Crumbed Fish")
    print("All meals come with a drink.")


main()
