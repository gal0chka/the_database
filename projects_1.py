import os


class Book:
    def __init__(self, id, title, author, data, rating):
        self.id = id
        self.title = title
        self.author = author
        self.data = data
        self.rating = rating


class Base:
    def __init__(self):
        self.arr = []

    def add_book(self, book, filename):
        self.arr.append(book)
        self.save_to_file(filename)

    def get_book_id(self, book_id):
        for el in self.arr:
            if str(el.id) == str(book_id):
                return el
        return None

    def get_all_info(self):
        if len(self.arr) == 0:
            print("Книг нет")
            return
        for el in self.arr:
            print(f"Id: {el.id}, Название: {el.title}, Автор книги: {el.author},"
                  f" Дата прочтения: {el.data}, Рейтинг книги: {el.rating}")

    def change_information(self, book_id, filename):
        book = self.get_book_id(book_id)
        if book is None:
            print("Книги с таким id нет")
            return
        print(f"Текущие данные: Id: {book.id}, Название: {book.title}, Автор книги: {book.author},"
              f" Дата прочтения: {book.data}, Рейтинг книги: {book.rating}")
        print("Введите новую информацию для книги:")
        book.title = input("Название: ")
        book.author = input("Автор: ")
        book.data = input("Дата прочтения: ")
        book.rating = input("Рейтинг: ")
        self.save_to_file(filename)

    def delete_book(self, book_id, filename):
        self.arr = [book for book in self.arr if str(book.id) != str(book_id)]
        self.save_to_file(filename)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for book in self.arr:
                file.write(f"{book.id}\n{book.title}\n{book.author}\n{book.data}\n{book.rating}\n")
        print("Данные сохранены в файл")

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print("Файл не найден")
            return
        with open(filename, 'r', encoding='utf-8') as file:
            self.arr = []
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                book_id = lines[i].strip()
                title = lines[i + 1].strip()
                author = lines[i + 2].strip()
                data = lines[i + 3].strip()
                rating = lines[i + 4].strip()
                book = Book(book_id, title, author, data, rating)
                self.arr.append(book)
        print("Данные загружены из файла")


def menu():
    print("Бесполезная сточка кода")
    print("Выйти: 0")
    print("Добавить книгу: 1")
    print("Получить книгу по индексу: 2")
    print("Показать все книги: 3")
    print("Изменить информацию по id: 4")
    print("Удалить книгу по id: 5")
    print("Загрузить базу из файла: 6")


def main():
    base = Base()
    filename = "books.txt"
    base.load_from_file(filename)

    while True:
        menu()
        try:
            ans = int(input())
        except ValueError:
            print("Введите число")
            continue
        if ans == 0:
            return
        elif ans == 1:
            id = input("Введите id: ")
            title = input("Введите название: ")
            author = input("Введите автора: ")
            data = input("Введите дату прочтения: ")
            rating = input("Введите рейтинг книги: ")
            el = Book(id, title, author, data, rating)
            base.add_book(el, filename)
        elif ans == 2:
            book_id = input("Введите id книги: ")
            book = base.get_book_id(book_id)
            if book is None:
                print("Данного id нет")
            else:
                print(f"Id: {book.id}, Название: {book.title}, Автор книги: {book.author},"
                      f" Дата прочтения: {book.data}, Рейтинг книги: {book.rating}")
        elif ans == 3:
            base.get_all_info()
        elif ans == 4:
            id = input("Какую книгу изменить по id: ")
            base.change_information(id, filename)
        elif ans == 5:
            book_id = input("Введите id книги: ")
            base.delete_book(book_id, filename)
        elif ans == 6:
            base.load_from_file(filename)


if __name__ == "__main__":
    main()
