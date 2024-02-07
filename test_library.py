import pytest

from customer import Customer
from library import Library


def test_init():
    library = Library()
    assert type(library.customers) is list
    assert library.customers == []
    assert type(library.booklist) is list
    assert library.booklist == []

def test_add_customers(library_empty, customer_a, customer_b):
    assert len(library_empty.customers) == 2
    assert customer_a in library_empty.customers
    assert customer_b in library_empty.customers

@pytest.fixture
def library_empty():
    return Library()

@pytest.fixture
def library_customers(library_empty):
    return Library()

@pytest.fixture
def customer_a(library_empty):
    return Customer('Hanna', None, library_empty)

@pytest.fixture
def customer_b(library_empty):
    return Customer('Edy', None, library_empty)
