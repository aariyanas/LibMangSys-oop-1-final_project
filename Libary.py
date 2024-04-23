'''
Progam Header
Program Name:Libary management system
Description:Code that finds books.
Author: Logan
'''
# Import Modules
import os
import csv
from book import Book
# Declare constants
MENU_DELIMITER = "="
CATALOG_DELIMITER = "-"
VALID_MENU_SELECTION = ['0', '1', '2', '3', '2130']
VALID_LIBRARIAN_MENU_SELECTION = ['0', '1', '2', '3', '4', '5', '6']

#Functions
def main():
    print("Starting the system ...")
    file_path = input("Enter book catalog filename: ")
    while not os.path.exists(file_path):
        file_path = input("File not found. Re-enter book catalog filename: ")
    book_list = load_books(file_path)

    menu_selection = print_menu()
    while menu_selection != '0':
        if menu_selection == '1':
            print("\n-- Search for books --")
            search_value = input("Enter search value: ")
            books_found_list = search_books(book_list, search_value)
            if len(books_found_list) == 0:
                print('No matching books found')
            else:
                print_books(books_found_list)
            menu_selection = print_menu()
        elif menu_selection == '2':
            borrow_book(book_list)
            menu_selection = print_menu()
        elif menu_selection == '3':
            return_book(book_list)
            menu_selection = print_menu()
        elif menu_selection == '2130':
            menu_selection = print_librarian_menu()
            while menu_selection != '0':
                if menu_selection == '1':
                    print("-- Search for books --")
                    search_value = input("Enter search value: ")
                    books_found_list = search_books(book_list, search_value)
                    print_books(books_found_list)
                    menu_selection = print_librarian_menu()
                elif menu_selection == '2':
                    borrow_book(book_list)
                    menu_selection = print_librarian_menu()
                elif menu_selection == '3':
                    return_book(book_list)
                    menu_selection = print_librarian_menu()
                elif menu_selection == '4':
                    add_book(book_list)
                    menu_selection = print_librarian_menu()
                elif menu_selection == '5':
                    remove_book(book_list)
                    menu_selection = print_librarian_menu()
                elif menu_selection == '6':
                    print("\n" + CATALOG_DELIMITER * 2 + ' Print book catalog ' + CATALOG_DELIMITER * 2)
                    print_books(book_list)
                    menu_selection = print_librarian_menu()
    save_books(book_list, file_path)
    print("\n" + CATALOG_DELIMITER * 2 + " Exit the system " + CATALOG_DELIMITER * 2)
    print("Book catalog has been saved.\nGood Bye!")

def load_books(file_path):
    book_list = []
    file_obj = None
    try:
        file_obj = open(file_path, 'r')
    except FileNotFoundError:
        print("File not found.")
        return book_list

    for line in file_obj:
        items = line.strip().split(',')
        if len(items) < 5:
            print("Error: Line does not contain enough elements.")
            continue
        availability = items[4].strip().lower() == 'true'
        book_obj = Book(items[0].strip(), items[1].strip(), items[2].strip(), int(items[3]), availability)
        book_list.append(book_obj)
    print(f"Book catalog has been loaded with {len(book_list)} books.")
    file_obj.close()
    return book_list

def print_menu():
    print("\nReader's Guild Library - Main Menu")
    print(MENU_DELIMITER * 34)
    print("1. Search for books\n2. Borrow a book\n3. Return a book\n0. Exit the system")
    menu_selection = input("Enter your selection: ")
    while menu_selection not in VALID_MENU_SELECTION:
        print("Invalid option")
        menu_selection = input("Enter your selection: ")
    return menu_selection

def print_librarian_menu():
    print("\nReader's Guild Library - Librarian Menu")
    print(MENU_DELIMITER * 39)
    print("1. Search for books\n2. Borrow a book\n3. Return a book\n4. Add a book\n5. Remove a book\n6. Print catalog\n0. Exit the system")
    menu_selection = input("Enter your selection: ")
    while menu_selection not in VALID_LIBRARIAN_MENU_SELECTION:
        print("Invalid option")
        menu_selection = input("Enter your selection: ")
    return menu_selection

def search_books(book_list, search_value):
    search_result_list = []
    for book_obj in book_list:
        book_obj_items = []
        book_obj_items.append(str(book_obj.get_isbn()).lower())
        book_obj_items.append(str(book_obj.get_title()).lower())
        book_obj_items.append(str(book_obj.get_author()).lower())
        book_obj_items.append(str(book_obj.get_genre_name()).lower())
        if search_value.lower() in ''.join(book_obj_items):
            search_result_list.append(book_obj)
    return search_result_list

def borrow_book(book_list):
    print("\n" + CATALOG_DELIMITER * 2 + ' Borrow a book ' + CATALOG_DELIMITER * 2)
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    isbn_book_research = find_book_by_isbn(book_list, isbn)
    if isbn_book_research != -1:
        if not book_list[isbn_book_research].get_available():
            print(f"'{book_list[isbn_book_research].get_title()}' with ISBN {book_list[isbn_book_research].get_isbn()} is not currently available.")
        else:
            book_list[isbn_book_research].borrow_it()
            print(f"'{book_list[isbn_book_research].get_title()}' with ISBN {book_list[isbn_book_research].get_isbn()} successfully borrowed.")
    else:
        print("No book found with that ISBN.")

def find_book_by_isbn(book_list, isbn):
    for index, book_obj in enumerate(book_list):
        if book_obj.get_isbn() == isbn:
            return index
    return -1

def return_book(book_list):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    search_result_index = find_book_by_isbn(book_list, isbn)
    if search_result_index == -1:
        print("No book found with that ISBN.")
    else:
        if not book_list[search_result_index].get_available():
            book_list[search_result_index].return_it()
            print(f'"{book_list[search_result_index].get_title()}" with ISBN {book_list[search_result_index].get_isbn()} successfully returned.')
        else:
            print(f'"{book_list[search_result_index].get_title()}" with ISBN {book_list[search_result_index].get_isbn()} is not currently borrowed.')

def add_book(book_list):
    new_isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    new_title = input("Enter title: ")
    new_author = input("Enter author name: ")
    new_genre = input("Enter genre: ")
    while new_genre not in Book.GENRE_DICT.values():
        print("Invalid genre. Choices are:", ', '.join(Book.GENRE_DICT.values()))
        new_genre = input("Enter genre: ")
    new_genre_key = list(Book.GENRE_DICT.values()).index(new_genre)

    new_book = Book(new_isbn, new_title, new_author, new_genre_key, True)
    book_list.append(new_book)
    print(f"'{new_book.get_title()}' with ISBN {new_book.get_isbn()} successfully added.")


def remove_book(book_list):
    print("\n" + CATALOG_DELIMITER * 2 + ' Remove a book ' + CATALOG_DELIMITER * 2)
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    book_index_to_remove = find_book_by_isbn(book_list, isbn)
    if book_index_to_remove != -1:
        book_removed = book_list.pop(book_index_to_remove)
        print(f"'{book_removed.get_title()}' with ISBN {book_removed.get_isbn()} successfully removed.")
    else:
        print("No book found with that ISBN.")

def print_books(book_list):
    print(f'{"ISBN":<15} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<12}')
    print(f'{CATALOG_DELIMITER * 14}  {CATALOG_DELIMITER * 25} {CATALOG_DELIMITER * 25} {CATALOG_DELIMITER * 20} {CATALOG_DELIMITER * 12}')
    for book_obj in book_list:
        print(f"{book_obj.get_isbn():<15} {book_obj.get_title():<25} {book_obj.get_author():<25} {book_obj.get_genre_name():<20} {'Available' if book_obj.get_available() else 'Borrowed':<12}")

def save_books(book_list, file_path):
    with open(file_path, 'w') as file_obj:
        writer = csv.writer(file_obj)
        for book_obj in book_list:
            writer.writerow([book_obj.get_isbn(), book_obj.get_title(), book_obj.get_author(), book_obj.get_genre(), book_obj.get_available()])
    print("Book catalog has been saved.")

if __name__ == "__main__":
    main()