import click
import requests


@click.command()
def main():
    choice = None

    while choice != "q":
        click.clear()
        click.echo("Menu:")
        click.echo("1. Search books by Works API")
        click.echo("2. Search books by Editions API")
        click.echo("3. Search books by ISBN API")
        click.echo("4. Search books by Book API - query params: `bibkeys`")
        click.echo("q. Quit")

        choice = click.prompt("\nEnter your choice")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()


def option1():
    """
    Search books by Works API
    """
    print("\nSearch books by Works API.....e.g. 'OL45804W', 'OL7353617M' etc...")
    id = click.prompt("Enter ID")
    try:
        response = requests.get(f"https://openlibrary.org/works/{id}.json")
        print("\n", response.json())
    except requests.exceptions.ConnectionError as e:
        print(f"\n\nError trying to connect to Openlibrary API: {e}")
    input("\n\nPress any key to continue...")


def option2():
    """
    Search books by Editions API
    """
    print("\nSearch books by Editions API.....e.g. 'OL45804W', 'OL7353617M' etc...")
    id = click.prompt("Enter ID")
    try:
        response = requests.get(f"https://openlibrary.org/books/{id}.json")
        print("\n", response.json())
    except requests.exceptions.ConnectionError as e:
        print(f"\n\nError trying to connect to Openlibrary API: {e}")
    input("\n\nPress any key to continue...")


def option3():
    """
    Search books by ISBN API
    """
    print("\nSearch books by ISBN.....e.g. '9780140328721', '9788449433993', '1405933259' etc...")
    isbn = click.prompt("Enter ISBN No")

    try:
        response = requests.get(f"https://openlibrary.org/isbn/{isbn}.json/")
        print("\n", response.json())
    except requests.exceptions.ConnectionError as e:
        print(f"\n\nError trying to connect to Openlibrary API: {e}")
    input("\n\nPress any key to continue...")


def option4():
    """
    Search books by Books API - query params: `bibkeys`
    """
    print(
        "\nSearch books by BookAPI.....e.g. 'ISBN:0201558025', 'OCLC:1003656209', 'LCCN:93005405', 'OLID:OL8492069M', 'ISBN:0385472579,LCCN:62019420' etc..."
    )
    bibkeys = click.prompt("Enter bibkeys")
    params = {"bibkeys": bibkeys, "format": "json"}

    try:
        response = requests.get("https://openlibrary.org/api/books", params=params)
        print("\n", response.json())
    except requests.exceptions.ConnectionError as e:
        print(f"\n\nError trying to connect to Openlibrary API: {e}")
    input("\n\nPress any key to continue...")


if __name__ == "__main__":
    main()
