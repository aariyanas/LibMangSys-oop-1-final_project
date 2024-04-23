
# Define Book class
class Book:
    GENRE_DICT = {
        0: 'Romance',
        1: 'Mystery',
        2: 'Science Fiction',
        3: 'Thriller',
        4: 'Young Adult',
        5: "Children's Fiction",
        6: 'Self-help',
        7: 'Fantasy',
        8: 'Historical Fiction',
        9: 'Poetry'
    }
    # Constructors
   
    def __init__(self, isbn, title, author, genre, available):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
    # Getters
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_genre(self):
        return self.genre
    def get_available(self):
        return self.available
    def get_genre_name(self):
        return Book.GENRE_DICT.get(self.genre, "N/A")
    def get_availability(self):
        if self.available == True:
            return "Available"
        else:
            return "Borrowed"

    # Setters
    def set_isbn(self, isbn):
        self.isbn = isbn
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_genre(self, genre):
        self.genre = genre
    def borrow_it(self):
        self.available = False
    def return_it(self):
        self.available = True
    def str(self):
        return f'{self.isbn:<15} {self.title:<25} {self.author:<25} {Book.GENRE_DICT.values(self.genre):<20} {self.get_availability():<12}'