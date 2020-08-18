def main():
    player_name = input("What is your name?")
    player_greeting(player_name)


def player_greeting(name):
    print("Welcome to the game, {}".format(name))


main()
