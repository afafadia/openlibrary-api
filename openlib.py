import json

import requests

menu_options = {
    1: "Search Books by Author",
    2: "Option 2",
    3: "Option 3",
    4: "Option 4",
    5: "Exit",
}


def print_menu():
    import os

    os.system("clear")
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def option1():
    print("\nSearch Books by Author.....e.g. Ani Mestre")
    resp = requests.get("http://openlibrary.org/search.json?author=Ani+Mestre")
    print(json.dumps(resp.json(), indent=2))
    input("\n\nPress Enter to continue...")


def option2():
    print("Handle option 'Option 2'")
    input("\n\nPress Enter to continue...")


def option3():
    print("Handle option 'Option 3'")
    input("\n\nPress Enter to continue...")


def option4():
    print("Handle option 'Option 4'")
    input("\n\nPress Enter to continue...")


if __name__ == "__main__":
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
        except:
            input("\n\nWrong input. Numeric inputs only...")
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print("\nThanks message before exiting\n\n")
            exit()
        else:
            input("\nInvalid option. Please enter a number between 1 and 5.\n\n")
