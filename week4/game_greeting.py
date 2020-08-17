def main():
    player_name = input("What is your name?")
    player_greeting(player_name)


def player_greeting(player_name):
    print("Welcome to the game, {}".format(player_name))


main()
