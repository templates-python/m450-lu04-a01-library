from dataclasses import dataclass, field


@dataclass
class Book:
    """
    a book in the library
    """

    title: str
    isbn: str
    location: str = field(init=False)  # will be assigned by the librarian

    def __post_init__(self):
        if isinstance(self.title, property):
            raise TypeError('__init__() missing required argument: "title"')
        if isinstance(self.isbn, property):
            raise TypeError('__init__() missing required argument: "isbn"')
        self.location = None
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, value):
        self._isbn = value
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = value
