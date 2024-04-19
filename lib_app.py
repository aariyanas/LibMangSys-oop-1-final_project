### LIBRARY MANAGEMENT MODULE ###

# menu = {
#     1: "Search for books"
#     2: 
# }
from operator import indexOf
from book import *

#ALMOST --> (done)
def load_books(books,  pathname):
    """
    
    """

    books = []
    file = open(pathname, "r")
    next_line = file.readline()
    print(f"FIRST LINE {next_line}")
    while next_line:
        # book_info = next_line
        book_params = next_line.split(",")
        # book = Book(book_params[0], book_params[1], book_params[2], int(book_params[3]), bool(book_params[-1]))
        print(f"CHECK PARAMS {book_params}")
        book_isbn = book_params[0]
        book_title = book_params[1]
        book_author = book_params[2]
        book_genre = int(book_params[3])
        book_availability = bool(book_params[4])
        book = Book(book_isbn, book_title, book_author, book_genre, book_availability)
        # print(f"CHECK BOOK INFO AS STRINGGGGG {book.toString()}")
        # print(f"BOOK ID = {book.__getattribute__}")
        next_line = file.readline()
        # print(f"NEXT LINE {next_line}")

        books.append(book)
    file.close()

    # for b in books:
    #     print(b)

    return len(books)

    

    # with open(pathname) as file:
    #     while file.__next__() != "":
    #         book_info = file.readline()
    #         book_params = book_info.split(",")
    #         book = Book()



    # books = []
    # file = open(pathname, "r")
    # for line in file:
    #     book_info= line.split(",")
        
    #     book = Book(str(book_info[0]), str(book_info[1]), str(book_info[2]), int(book_info[3]), bool(book_info[-1]))
        
    #     print(book)
    #     # add_this_book = book.toString()
    #     books.append(book)

    #     #print("book added to list")
    # # for b in books:
    # #     print(b.toString())
    
    # file.close()        # input()
    #     #print(books)
    # # for b in books:
    # #     print(b)
    # # print(books)
    # # print(book.get_genre_name())


# before calling this function, input search string from user
# after calling this function, call print_books() passing to it the search result list

#WORKS
def search_books(books, search_by):
    """
    
    """
    contains_search_by = []
    for book in books:
        if search_by in book:
            contains_search_by.append(book)
    print(contains_search_by)
    return contains_search_by

#WORKS
def borrow_book(books):
    """
    
    """
    corresponding_isbn = input("Enter the isbn of the book you want to borrow: ")

    for book in books:
        if (find_book_by_isbn(books, corresponding_isbn) != -1) and book.get_availability():
            Book.borrow_it(book)


#WORKS
def find_book_by_isbn(books, isbn):
    """
    
    """
    for book in books:
        if book[0] == isbn or len(books) == 0:
            return book.index(books) #stub
    return -1    


def return_book(books):
    """
    
    """
    isbn = input("Enter the isbn of the book you want to return: ")
    book_exists = find_book_by_isbn(books, isbn)
    if (book_exists != -1):
        book = books[book_exists]
        if book.get_availability() == "Borrowed":
            book.return_it()
            print(f"{book.getTitle()} with ISBN {isbn} successfully returned")
        else:
            print("Nah, the book is borrowed, bitch. Yoooooo")
    else:
        print("No book with that isbn freakin exists you hooooo")
        

def add_book(books):
    """
    
    """
    isbn = input("Enter isbn: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    genres = [Book.ROMANCE, Book.MYSTERY, Book.SCI_FI, Book.THRILLER, Book.YOUNG_ADULT, Book.KID_FICTION, Book.SELF_HELP, Book.FANTASY, Book.HIST_FICTION, Book.POETRY]
    if genre not in genres:
        print("Invalid genre. Try the fuck again you ho")
        genre = input("Enter genre: ")
    else:
        book = Book(isbn, title, author, genre.index(genres))
        books.append(book)
        print("Book added youuuuu")


def remove_book(books):
    """
    
    """
    isbn = input("Enter isbn: ")   
    book = find_book_by_isbn(books, isbn)
    if (book != -1):
        books.remove(book)
    else:
        print("ISBN/boook of that title not found")


def print_books(books):
    """
    
    """
    print("INSERT BOOK INFO HEADING HERE")
    for book in books:
        print(book.toString() + "\n")


def save_books(books, pathname):
    """
    
    """
    file = open(pathname, "w")
    for book in books:
        to_write = f"{book[0]},{book[1]},{book[2]},{book[3],{book[4]}}"
        file.write(to_write)
    numBooks = len(file.readlines)
    file.close()
    return numBooks - 1





books_TEST = [["978-0060000000","To Kill a Mockingbird","Harper Lee",3,True], ["978-0140000000","Pride and Prejudice","Jane Austen",0,False], ["978-0320000000","The Catcher in the Rye","J.D. Salinger",4,True]]

# print(find_book_by_isbn(books, "978-0320000000"))
# search_books(books, "Pride and Prejudice")
# borrow_book(books)
load_books([], "books.csv")