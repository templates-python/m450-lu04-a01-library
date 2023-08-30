import random


class Library:
    """
    a library containing books and customers
    """

    def __init__(self):
        """
        default constructor
        """
        self.booklist = []
        self.customers = []

    def print_inventory(self):
        """
        prints the current inventory
        :return:
        """
        print('Inventar:')
        for book in self.booklist:
            print(book)
        print('---')

    def add_customer(self, customer):
        """
        adds a customer
        :param customer:
        :return:
        """
        self.customers.append(customer)

    def search_customer(self, name):
        """
        searches a customer by his name
        :param name:
        :return: Customer or None
        """
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def print_customer(self):
        """
        prints a list of all customers
        :return: None
        """
        print('Kunden:')
        for customer in self.customers:
            customer.print()
        print('---')

    def add_book(self, a_book):
        """
        adds a book to a random position in the library
        :param a_book:
        :return:
        """

        self.booklist.append(a_book)
        return chr(random.randint(65, 68)) + str(random.randint(1, 10))

    def remove_book(self, book):
        """
        removes a book from the library
        :param book:
        :return:
        """
        self.booklist.remove(book)

    def search_book_by_title(self, title):
        """
        searches a book by its name
        :param name:
        :return: Book or None
        """
        for book in self.booklist:
            if book.title == title:
                return book
        return None

    def take_book(self, location):
        """
        takes the book at the specified location from the library
        :param location:
        :return: Book
        """
        for book in self.booklist:
            if book.location == location:
                self.booklist.remove(book)
                return book

    def put_back_book(self, borrowed_book):
        """
        puts a book back into the library
        :param borrowed_book:
        :return:
        """
        self.booklist.append(borrowed_book)

    @property
    def booklist(self):
        return self._booklist

    @booklist.setter
    def booklist(self, value):
        self._booklist = value

    @property
    def customers(self):
        return self._customers

    @customers.setter
    def customer(self, value):
        self._customers = value
