from book import Book


class Librarian:
    """
    a librarian who manages the books in the library
    """

    def __init__(self, name, library):
        """
        constructor
        :param name: fullname of the librarian
        :param library: the library he manages
        """
        self._name = name
        self._library = library

    def buy_new_book(self, title, isbn):
        """
        buying and adding a new book to the library
        :param title:
        :param isbn:
        :return:
        """
        book = Book(title=title, isbn=isbn)
        location = self.library.add_book(book)
        book.location = location

    def borrow_a_book_by_title(self, customer, title):
        """
        the customer borrows a book identified by the title
        :param customer:
        :param title:
        :return: Book or None if not found
        """

        if customer.book is not None:
            print('Bring zuerst das ausgeliehene Buch zurück')
            raise ValueError('Nur 1 Buch pro Kunde')
        book = self.library.search_book_by_title(title)
        if book is None:
            print('Das angefragte Buch ist nicht vorhanden')
            raise ValueError('Buch nicht in Bibliothek')
        else:
            location = book.location
            book = self.library.take_book(location)
        return book

    def get_a_book_from_customer(self, borrowed_book):
        """
        puts the book back into the library
        :param borrowed_book:
        :return:
        """
        self.library.put_back_book(borrowed_book)

    def remind_customer(self, name):
        """
        reminds the customer to bring back the book
        :param name: customer's name
        :return:
        """
        print(f'Erinnerung für {name}')
        customer = self.library.search_customer(name)
        customer.remind()

    def remove_book(self, title):
        """
        permanently removes a book from the library
        :param title:
        :return:
        """
        print(f'\n---\nentferne Buch "{title}"')
        book = self.library.search_book_by_title(title)
        self.library.remove_book(book)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, value):
        self._library = value
