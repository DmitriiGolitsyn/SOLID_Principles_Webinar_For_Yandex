# Single Responsibility Principle (SRP)
# Принцип единственной ответственности
import datetime


# ------------------------------ 04 ------------------------------
# Сделаем лучше. Применяем паттерн фасад.


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
        print(f'Создали объект книга: "{self.title}" ({self.author}).')


class Library:
    books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

class BuhReports:

    def get_book_buh_info(self, book: Book):
        last_years = 5
        current_year = datetime.datetime.today().year
        quantity = (
            book.quantity
            if book.year >= (current_year - last_years)
            else 0
        )
        return f'{quantity} шт. "{book.title}" ({book.author})'

    def library_buh_report(self, books):
        print('Отчет для бухгалтера:')
        for book in books:
            print(self.get_book_buh_info(book), ': куплены по', book.price, 'руб.')
        print()


class StorageReports:

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

    def library_buh_report(self):
        buh_report = BuhReports()
        buh_report.library_buh_report(self.library.books)

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
new_book = Book(
    title='Изучаем Python',
    author='Марк Лутц',
    year=2020,
    price=35,
    quantity=11
)
library.add_book(new_book)
library.add_book(
    Book(
        title='Изучаем SQL',
        author='Майкл Смит',
        year=2010,
        price=50,
        quantity=7
    )
)
print()

library.library_buh_report()
library.library_storage_report()


