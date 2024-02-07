import pytest as pytest

from book import Book


def test_init_correct():
    """
    create a book with title and isbn
    """
    book = Book('My book', '978-8-456-01789-2')
    assert type(book) is Book
    assert book.title == 'My book'
    assert book.isbn == '978-8-456-01789-2'

@pytest.mark.xfail
def test_init_wrong():
    """
    create a book with one value or none
    """
    book = Book('wrong')

def test_output(book1):
    """
    check the output when printing a book
    """
    assert book1.__str__() == 'Book(title=\'First book\', isbn=\'978-1-111-11111-1\', location=None)'

def test_location_1(book1):
    """
    is location empty when creating a book with title and isbn
    """
    assert type(book1) is Book
    assert book1.location is None

def test_location_2():
    """
    is location empty when creating a book with title, isbn and location
    """
    book = Book('The location', '978-1-111-11111-1', 'shelf a1')
    assert type(book) is Book
    assert book.location is None

@pytest.fixture
def book1():
    return Book('First book', '978-1-111-11111-1')
