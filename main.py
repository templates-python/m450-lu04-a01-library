from customer import Customer
from librarian import Librarian
from library import Library


def main():
    print("Bibliotheks-Anwendung\n=====================\n")
    library = Library()
    pit = Librarian('Pit', library)
    moritz = Customer('Moritz', pit, library)
    ursula = Customer('Ursula', pit, library)
    pit.buy_new_book(title='Ich bin dann mal weg', isbn='3-345-678')
    pit.buy_new_book(title='im Westen nichts neues', isbn='6-444-856')
    pit.buy_new_book(title='Das Omen', isbn='3-3345-678-X')
    pit.buy_new_book(title='Harry Potter, die neue Welt', isbn='3-4321-334')
    pit.buy_new_book(title='die schönsten Zugreisen', isbn='3-2123-554')
    ursula.borrow_a_book_by_title('Das Omen')
    ursula.borrow_a_book_by_title('Das Omen')
    moritz.borrow_a_book_by_title('Ich bin dann mal weg')
    ursula.bring_back_a_book()
    pit.remind_customer('Moritz')
    pit.remove_book('Harry Potter, die neue Welt')
    ursula.borrow_a_book_by_title('Das nie geschriebene Buch')

    library.print_customer()
    library.print_inventory()


if __name__ == '__main__':
    main()
