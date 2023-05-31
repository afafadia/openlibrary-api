# https://openlibrary.org/dev/docs/api/books

The above URL mentions retrieving books information by using 4 different types of API's:

1.  The  **Works**  API (by Work ID)
2.  The  **Editions**  API (by Edition ID)
3.  The  **ISBN**  API (by ISBN)  
4.  The  **Books**  API (generic)


# Code Walkthrough

1. After cloning the repository to a suitable folder location, navigate to the folder and do the following:
	a. Activate virtual environment e.g., by running the command: "source ~/<foldername>/venv/bin/activate"
	b. Make sure you have "requests", "click" pypi packages installed in the virtual environment
	b. Run the code by the command: "python openlib.py"

## Menu

It will show you menu with 4 options:

Menu:
1. Search books by Works API
2. Search books by Editions API
3. Search books by ISBN API
4. Search books by Book API - query params: `bibkeys`

  q. Quit

Enter your choice: 

## Option 1: Search books by Works API

Upon selecting this option from the menu, it will request you to enter the Work ID - you can enter any valid Work ID that you know OR you may use the sample ID's provided above the Work ID input field and hit "Enter"


## Option 2: Search books by Editions API

Upon selecting this option from the menu, it will request you to enter the Edition ID - you can enter any valid Edition ID that you know OR you may use the sample ID's provided above the Edition ID input field and hit "Enter"

## Option 3: Search books by ISBN API

Upon selecting this option from the menu, it will request you to enter the ISBN ID - you can enter any valid ISBN ID that you know OR you may use the sample ID's provided above the ISBN No. input field and hit "Enter"

## Option 4: Search books by Books API

Upon selecting this option from the menu, it will request you to enter `bibkeys` params - you can enter any valid `bibkeys` params that you know OR you may use the sample params within the quotes provided above the `bibkeys` input field and hit "Enter"

## Option 'q': Quit menu & terminate

You may hit 'q' key on the keyboard to quit and terminate the program any time OR you may navigate through the menu if you want to pull more results using the above API's
