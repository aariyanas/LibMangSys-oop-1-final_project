### LIBRARY MANAGEMENT MODULE ###

# menu = {
#     1: "Search for books"
#     2: 
# }
from operator import indexOf
from book import *


def load_books(books,  pathname):
    """
    
    """
    books = []
    file = open(pathname, "r")
    for line in file:
        book_info = line.strip()
        book = Book(book_info[0], book_info[1], book_info[2], book_info[3], book_info[-1])
        books.append(book)
        print("book added to list")

        print(books)
    # for b in books:
    #     print(b)
    # print(books)
    # print(book.get_genre_name())

# before calling this function, input search string from user
# after calling this function, call print_books() passing to it the search result list
def search_books(books, search_by):
    """
    
    """
    contains_search_by = []
    for book in books:
        if search_by in book:
            contains_search_by.append(book)
    print(contains_search_by)
    return contains_search_by

def borrow_book(books):
    """
    
    """
    corresponding_isbn = input("Enter the isbn of the book you want to borrow: ")

    for book in books:
        if (find_book_by_isbn(books, corresponding_isbn) != -1) and Book.get_availability(book):
            Book.borrow_it(book)


def find_book_by_isbn(books, isbn):
    """
    
    """
    for book in books:
        if book[0] == isbn or len(books) == 0:
            return indexOf(books, book) #stub
    return -1    


books = [["978-0060000000","To Kill a Mockingbird","Harper Lee",3,True], ["978-0140000000","Pride and Prejudice","Jane Austen",0,False], ["978-0320000000","The Catcher in the Rye","J.D. Salinger",4,True]]

find_book_by_isbn(books, "978-0320000000")
search_books(books, "Jane Austen")
borrow_book(books)