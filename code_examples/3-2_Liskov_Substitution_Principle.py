# Liskov Substitution Principle (LSP)
# Принцип подстановки Барбары Лисков
import datetime
from abc import abstractmethod


# ------------------------------ 02 ------------------------------
# Или может лучше переписать код один раз, используя LSP?

class Item:
    price: float
    quantity: int
    type_name: str

    @abstractmethod
    def get_info(self):
        pass


class Newspaper(Item):
    title: str
    year: int
    number: int
    type_name = 'газета'

    def __init__(self, title, year, number, price, quantity):
        self.title = title
        self.year = year
        self.number = number
        self.price = price
        self.quantity = quantity
        print(
            f'Создали объект {self.type_name}: '
            f'"{self.title}", номер ({self.number})'
        )

    def get_info(self):
        return (
            f'{self.type_name} "{self.title}" '
            f'({self.year} год, номер {self.number})'
        )


class Book(Item):
    title: str
    author: str
    year: int
    type_name = 'книга'

    def __init__(self, title, author, price, year, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.quantity = quantity
        print(
            f'Создали объект {self.type_name}: '
            f'"{self.title}" ({self.author})'
        )

    def get_info(self):
        return (
            f'{self.type_name} "{self.title}" ({self.author})'
        )


class Journal(Item):
    title: str
    year: int
    number: int
    type_name = 'журнал'

    def __init__(self, title, year, number, price, quantity):
        self.title = title
        self.year = year
        self.number = number
        self.price = price
        self.quantity = quantity
        print(
            f'Создали объект {self.type_name}: '
            f'"{self.title}", номер ({self.number})'
        )

    def get_info(self):
        return (
            f'{self.type_name} "{self.title}" '
            f'({self.year} год, номер {self.number})'
        )


class Library:
    items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)


class BuhReports:

    def get_buh_item_info(self, item: Item):
        last_years = 5
        current_year = datetime.datetime.today().year
        quantity = (
            item.quantity
            if item.year >= (current_year - last_years)
            else 0
        )
        return f'{quantity} шт. {item.get_info()}'

    def library_buh_report(self, library: Library):
        print('Отчет для бухгалтера:')
        for item in library.items:
            print(self.get_buh_item_info(item), ': куплены по', item.price, 'руб.')
        print()


class StorageReports:

    def get_storage_item_info(self, item: Item):
        return f'{item.quantity} шт. {item.get_info()}'

    def library_storage_report(self, library):
        print('Отчет для библиотекаря:')
        for item in library.items:
            print('На полках', self.get_storage_item_info(item))
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
        buh_report = BuhReports()
        buh_report.library_buh_report(self.library)

    def library_storage_report(self):
        bibliotkar_report = StorageReports()
        bibliotkar_report.library_storage_report(self.library)

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
library.add_item(
    Newspaper(
        title='Python Daily',
        year=2023,
        number=22,
        price=1,
        quantity=2
    )
)
print()

library.library_buh_report()
library.library_storage_report()
