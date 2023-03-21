# Dependency Inversion Principle (DIP)
# Принцип инверсии зависимостей
import datetime
from abc import abstractmethod, ABC


# ------------------------------ 01 ------------------------------
# Зависимость от конкретной реализации


class Item(ABC):
    price: float
    quantity: int
    type_name: str
    year: int

    @abstractmethod
    def get_info(self):
        pass


class Newspaper(Item):
    title: str
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

    def _get_buh_item_info(self, item: Item):
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
            print(self._get_buh_item_info(item), ': куплены по', item.price, 'руб.')
        print()


class StorageReports:

    def _get_storage_item_info(self, item: Item):
        return f'{item.quantity} шт. {item.get_info()}'

    def library_storage_report(self, library):
        print('Отчет для библиотекаря:')
        for item in library.items:
            print('На полках', self._get_storage_item_info(item))
        print()


class DataKeeperMySQL:

    def _connect_to_mysql(self):
        print(f'Подключились к БД MySQL.')

    def save_all_to_mysql(self):
        self._connect_to_mysql()
        print(f'Сохранено в БД MySQL.')

    def get_all_from_mysql(self):
        self._connect_to_mysql()
        print(f'Загружено из БД MySQL.')


class BaseUser(ABC):
    name: str
    password: str

    def __init__(self, name, password):
        self.name = name
        self.password = password
        print(f'Пользователь с именем {self.name} создан.')


class LibraryUser(BaseUser):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.library = Library()


class LibraryEditorMixin(ABC):
    def add_item(self, item: Item):
        self.library.add_item(item)


class BuhReportMixin(ABC):
    def library_buh_report(self):
        buh_report = BuhReports()
        buh_report.library_buh_report(self.library)


class BibliotekarReportMixin(ABC):
    def library_storage_report(self):
        bibliotekar_report = StorageReports()
        bibliotekar_report.library_storage_report(self.library)


class BuhgalterRoleInterface(LibraryUser, LibraryEditorMixin, BuhReportMixin, DataKeeperMySQL):
    ...


class BibliotekarRoleInterface(LibraryUser, LibraryEditorMixin, BibliotekarReportMixin, DataKeeperMySQL):
    ...


class UserManagerInterface(ABC):
    @abstractmethod
    def create_user(self, name, password, user_role):
        pass


class UserManager(UserManagerInterface):
    def create_user(self, name, password, user_role):
        user_interface = user_role(name, password)
        return user_interface


user_manager = UserManager()
buhgalter = user_manager.create_user(
    name="Анна Николаевна",
    password='123',
    user_role=BuhgalterRoleInterface
)
bibliotekar = user_manager.create_user(
    name="Ольга Владимировна",
    password='клеопатра',
    user_role=BibliotekarRoleInterface
)
print()

bibliotekar.add_item(
    Book(
        title='Изучаем SQL',
        author='Майкл Смит',
        year=2010,
        price=50,
        quantity=7
    )
)
bibliotekar.add_item(
    Journal(
        title='Программист',
        year=2023,
        number=1,
        price=10,
        quantity=5
    )
)
buhgalter.add_item(
    Newspaper(
        title='Python Daily',
        year=2023,
        number=22,
        price=1,
        quantity=2
    )
)
print()

buhgalter.library_buh_report()
bibliotekar.library_storage_report()

buhgalter.save_all_to_mysql()
print()
bibliotekar.get_all_from_mysql()
