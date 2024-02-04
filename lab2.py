BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError('Должно быть число')
        if id_ <= 0:
            raise ValueError('ID больше нуля')
        if not isinstance(name, str):
            raise TypeError('Должно быть название прописью')
        if not isinstance(pages, int):
            raise TypeError('Страницы должны быть числом')
        if pages <= 0:
            raise ValueError('Страниц всегда больше нуля')
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга {self.name!r}'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None):
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        # id = self.books
        # # max_ = 0
        # # for book in self.books:
        # # #     if max_ < book.id:
        # # #         max_ = book.id
        # # # return max_ + 1
        return max(self.books, key=lambda book: book.id).id + 1

    def get_index_by_book_id(self, id_):
        if not isinstance(id_, int):
            raise TypeError('Должно быть число')
        if id_ <= 0:
            raise ValueError('ID больше нуля')
        for i, book in enumerate(self.books):
            if book.id == id_:
                return i
        raise ValueError('нет такой книги')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
