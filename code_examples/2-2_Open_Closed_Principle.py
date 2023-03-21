# Open/Closed Principle (OCP)
# Принцип открытости/закрытости
import datetime


# ------------------------------ 02 ------------------------------
# Рефакторим, применяя принцип открытости/закрытости

class Item:
    price: float
    quantity: int


class Book(Item):
    title: str
    author: str
    year: int

    def __init__(self, title, author, price, year, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.quantity = quantity
        print(f'Создали объект книга: "{self.title}" ({self.author})')


class Journal(Item):
    title: str
    year: int
    number: int

    def __init__(self, title, year, number, price, quantity):
        self.title = title
        self.year = year
        self.number = number
        self.price = price
        self.quantity = quantity
        print(f'Создали объект журнал: "{self.title}", номер ({self.number})')


class Library:
    items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)


class BuhReports:
    # Пока не работает
    def get_book_buh_info(self, book: Book):
        last_years = 5
        current_year = datetime.datetime.today().year
        quantity = (
            book.quantity
            if book.year >= (current_year - last_years)
            else 0
        )
        return f'{quantity} шт. Книга "{book.title}" ({book.author})'

    def get_journal_buh_info(self, journal: Journal):
        last_years = 5
        current_year = datetime.datetime.today().year
        quantity = (
            journal.quantity
            if journal.year >= (current_year - last_years)
            else 0
        )
        return (
            f'{quantity} шт. Журнал "{journal.title}" '
            f'(год {journal.year}, номер {journal.number})'

        )

    def library_buh_report(self, books, journals):
        print('Отчет для бухгалтера:')
        for book in books:
            print(self.get_book_buh_info(book), ': куплены по', book.price, 'руб.')
        for journal in journals:
            print(self.get_journal_buh_info(journal), ': куплены по', journal.price, 'руб.')
        print()


class StorageReports:
    # Пока не работает
    def add_book(self, book: Book):
        self.books.append(book)

    def get_book_storage_info(self, book: Book):
        return f'{book.quantity} шт. "{book.title}" ({book.author})'

    def library_storage_report(self, books):
        print('Отчет для библиотекаря:')
        for book in books:
            print('На полках', self.get_book_storage_info(book))
        print()


class Saver:

    def save_all_books(self, library: Library):
        # Сохраняем в базу данных
        print(f'Книги cохранены в базе данных.')

    def get_all_books(self) -> Library:
        #  Получаем из базы данных
        print(f'Книги загружены из базы данных.')


class LibraryFacade:
    def __init__(self):
        self.library = Library()

    def add_item(self, item: Item):
        self.library.add_item(item)

    def library_buh_report(self):
        ...

    def library_storage_report(self):
        ...

    def save_all_books(self):
        ...

    def get_all_books(self) -> Library:
        ...


library = LibraryFacade()
library.add_item(
    Book(
        title='Изучаем SQL',
        author='Майкл Смит',
        year=2010,
        price=50,
        quantity=7
    )
)
library.add_item(
    Journal(
        title='Программист',
        year=2023,
        number=1,
        price=10,
        quantity=5
    )
)
print()

for item in library.library.items:
    print(f'{item.title} - {type(item)}')
