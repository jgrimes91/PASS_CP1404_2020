"""
This program is to help track what shows the user is watching on Netflix.
"""
from operator import itemgetter

SHOWS = "shows.csv"
MENU = "Menu: \nL - List all shows\nA - Add new show\nM - Mark a show as watched\nQ - Quit"


def main():
    """
    :return:
    """
    print("PASS CP1404 Netflix Tracker")
    shows = []
    shows_file = open("shows.csv")
    for line in shows_file:
        shows.append(line.strip().split(","))
    shows_file.close()

    print(shows)

    count = len(shows)
    print("{} shows loaded".format(count))

    user_input = " "

    while user_input != "Q":
        print(MENU)
        user_input = input(">>> ").upper()
        if user_input == "L":
            # print("List shows")
            display_shows(shows)
        elif user_input == "A":
            print("###Add a show")
            add_show(shows)
        elif user_input == "M":
            print("###Mark a show as completed")
            # mark_shows()
        elif user_input == "Q":
            print("###Saving shows and quit program")
            # save_shows()
        else:
            print("Invalid choice")


def display_shows(shows):
    shows.sort(key=itemgetter(0))

    string_format = "{} {}. {:{}} Seasons: {:1}"
    title_length = find_length(0, shows)
    for i in range(0, len(shows)):
        complete = " "
        if shows[i][-1] == "c":
            complete = "*"
        print(string_format.format(complete, i + 1, shows[i][0], title_length, shows[i][1]))


def find_length(column, table):
    max_width = 0
    for row in table:
        current_width = len(row[column])
        if current_width > max_width:
            max_width = current_width
    return max_width + 5


def add_show(shows):
    new_show = []
    title = input("Title: ")
    new_show.append(title)
    season = int(input("Season: "))
    new_show.append(season)
    shows.append(new_show)
    new_show.append("w")


main()
