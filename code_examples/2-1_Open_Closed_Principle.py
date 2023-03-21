# Open/Closed Principle (OCP)
# Принцип открытости/закрытости
import datetime


# ------------------------------ 01 ------------------------------
# Администрация библиотеки решила расширить ассортимент
# и просит добавить еще журналы


class Book:
    title: str
    author: str
    year: int
    price: float
    quantity: int

    def __init__(self, title, author, price, year, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.quantity = quantity
        print(f'Создали объект книга: "{self.title}" ({self.author})')


class Journal:
    title: str
    year: int
    number: int
    price: float
    quantity: int

    def __init__(self, title, year, number, price, quantity):
        self.title = title
        self.year = year
        self.number = number
        self.price = price
        self.quantity = quantity
        print(f'Создали объект журнал: "{self.title}", номер ({self.number})')


class Library:
    books: list[Book] = []
    journals: list[Journal] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_journal(self, journal: Journal):
        self.journals.append(journal)


class BuhReports:

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
    # Пока изменяли отчеты для бухгалтера, поняли, что что-то не так.
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

    def add_book(self, book: Book):
        self.library.add_book(book)

    def add_journal(self, journal: Journal):
        self.library.add_journal(journal)

    def library_buh_report(self):
        buh_report = BuhReports()
        buh_report.library_buh_report(
            self.library.books,
            self.library.journals
        )

    def library_storage_report(self):
        bibliotkar_report = StorageReports()
        bibliotkar_report.library_storage_report(self.library.books)

    def save_all_books(self):
        saver = Saver()
        saver.save_all_books(self.library.books)

    def get_all_books(self) -> Library:
        saver = Saver()
        return saver.get_all_books()


library = LibraryFacade()
library.add_book(
    Book(
        title='Изучаем SQL',
        author='Майкл Смит',
        year=2010,
        price=50,
        quantity=7
    )
)
library.add_journal(
    Journal(
        title='Программист',
        year=2023,
        number=1,
        price=10,
        quantity=5
    )
)
print()

library.library_buh_report()
# library.library_storage_report()


