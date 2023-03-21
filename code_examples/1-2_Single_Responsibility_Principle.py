# Single Responsibility Principle (SRP)
# Принцип единственной ответственности
import datetime


# ------------------------------ 02 ------------------------------
# От бухгалтера поступило задание:
# - Нужно в отчете для книг, которым менее 5 лет выводить количество 0.


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

    def get_book_info(self, book: Book):
        last_years = 5
        current_year = datetime.datetime.today().year
        quantity = (
            book.quantity
            if book.year >= (current_year - last_years)
            else 0
        )
        return f'{quantity} шт. "{book.title}" ({book.author})'

    def library_buh_report(self):
        print('Отчет для бухгалтера:')
        for book in self.books:
            print(self.get_book_info(book), ': куплены по', book.price, 'руб.')
        print()

    def library_storage_report(self):
        print('Отчет для библиотекаря:')
        for book in self.books:
            print('На полках', self.get_book_info(book))
        print()

    def save_all_books(self):
        # Сохраняем в базу данных
        print(f'Книги cохранены в базе данных.')

    def get_all_books(self):
        # Получаем из базы данных
        print(f'Книги загружены из базы данных.')


library = Library()
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

# library.save_all_books()
# library.get_all_books()
