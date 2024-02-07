from dataclasses import dataclass


@dataclass
class Customer:
    """
    a customer who can borrow or bring back one book
    """

    def __init__(self, name, librarian, library):
        """
        constructor for a customer
        :param name:
        :param librarian:
        :param library:
        """
        self._name = name
        self._reminded = False
        self._librarian = librarian
        self._book = None
        library.add_customer(self)

    def print(self):
        """
        prints the name of this customer
        :return:
        """
        print(f'Kunde: {self.name}')

    def borrow_a_book_by_title(self, title):
        """
        tells the librarian to lend a book identified by the title
        :param title: the title of the book to borrow
        :return: boolean
        """

        try:
            self.book = self.librarian.borrow_a_book_by_title(self, title)
            print(f'{self.name} hat das Buch "{self.book.title}" erhalten.')
            return True
        except ValueError:
            return False

    def bring_back_a_book(self):
        """
        returns a book to the librarian
        :return: boolean
        """
        try:
            print(f'{self.name} hat das Buch "{self.book.title}" zurückgebracht.')
            self.librarian.get_a_book_from_customer(self.book)
            self.book = None
            self.reminded = False
            return True
        except:
            print('Du hast gar kein Buch ausgeliehen.')
            return False

    def remind(self):
        """
        Reminde the customer about a borrowed book
        """
        self.reminded = True
        print(f'Das Buch "{self.book.title}" ist noch ausstehend')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        self._book = value

    @property
    def reminded(self):
        return self._reminded

    @reminded.setter
    def reminded(self, value):
        self._reminded = value

    @property
    def librarian(self):
        return self._librarian

    @librarian.setter
    def librarian(self, value):
        self._librarian = value

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, value):
        self._library = value
