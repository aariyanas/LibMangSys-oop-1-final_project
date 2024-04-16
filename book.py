### BOOK CLASS ###

from typing import final

class Book:
    """
    Represents a Book with a specific title, author, genre, isbn, and whether it is available or not
    """
    ROMANCE: final = "Romance"  #0
    MYSTERY: final = "Mystery"  #1
    SCI_FI: final = "Science Fiction"   #2
    THRILLER: final = "Thriller"    #3
    YOUNG_ADULT: final = "Young Adult"  #4
    KID_FICTION: final = "Children's Fiction"   #5
    SELF_HELP: final = "Self-help"  #6
    FANTASY: final = "Fantasy"  #7
    HIST_FICTION: final = "Historical Fiction"  #8
    POETRY: final = "Poetry"    #9

    def __init__(self, isbn, title, author, genre, available):
        """
        
        """
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    def get_isbn(self):
        """
        
        """
        return self.__isbn
    
    def get_title(self):
        """
        
        """
        return self.__title
    
    def get_author(self):
        """
        
        """
        return self.__author
    
    def get_genre(self):
        """
        
        """
        return self._genre
    
    def is_available(self):
        """
        
        """
        return self.__available
    
    def get_genre_name(self):
        """
        
        """
        if self.__genre == 0:
            return self.ROMANCE
        elif self.__genre == 1:
            return self.MYSTERY
        elif self.__genre == 2:
            return self.SCI_FI
        elif self.__genre == 3:
            return self.THRILLER
        elif self.__genre == 4:
            return self.YOUNG_ADULT
        elif self.__genre == 5:
            return self.KID_FICTION
        elif self.__genre == 6:
            return self.SELF_HELP
        elif self.__genre == 7:
            return self.FANTASY
        elif self.__genre == 8:
            return self.HIST_FICTION
        elif self.__genre == 9:
            return self.POETRY
        
    def get_availability(self):
        """
        
        """
        if self.__available:
            return "Available"
        else:
            return "Borrowed"
        
    def set_isbn(self, this_isbn):
        """
        
        """
        self.__isbn == this_isbn

    def set_title(self, this_title):
        """
        
        """
        self.__title == this_title

    def set_author(self, this_author):
        """
        
        """
        self.__author == this_author

    def set_genre(self, this_genre):
        """
        
        """
        self.__genre == this_genre

    def borrow_it(self):
        """
        
        """
        self.__available == False

    def return_it(self):
        """
        
        """
        self.__available == True

    def __str__(self):
        """
        
        """
        return f"{self.__isbn} {self.__title}\t\t{self.__author}\t\t{self.__genre}\t{self.get_availability()}"




# book = Book("999-643503", "Life of Pi", "Yann Martel", 0, False)  #TESTER BOOK












