import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_added_book_genre_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_set_book_genre_existing_book_valid_genre_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_set_book_genre_existing_book_invalid_genre_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Семейный')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_set_book_genre_unexisting_book_valid_genre_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_get_book_genre_getting_not_empty_genre_from_existing_book(self, test_collection):
        assert test_collection.get_book_genre('Книга 4 Мультфильмы') == 'Мультфильмы'

    def test_get_books_with_specific_genre_get_2_books_from_preset_fixture_test_collection(self, test_collection):
        assert len(test_collection.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_created_dict_length_from_preset_fixture_test_collection_equal_7(self, test_collection):
        assert len(test_collection.get_books_genre()) == 7

    def test_get_books_for_children_books_for_children_from_preset_fixture_test_collection_not_include_books_with_genre_age_rating_or_not_in_genre_list(self, test_collection):
        assert len(test_collection.get_books_for_children()) == 3

    @pytest.mark.parametrize('name', ['Книга 1 Фантастика', 'Книга 2 Ужасы', 'Книга 7 без жанра'])
    def test_add_book_in_favorites_added_2_different_books_to_favorites_genre_may_be_empty(self, test_collection, name):
        test_collection.add_book_in_favorites(name)
        assert len(test_collection.favorites) == 1

    def test_delete_book_from_favorites_add_2_books_remove_1_and_1_left(self, test_collection):
        test_collection.add_book_in_favorites('Книга 1 Фантастика')
        test_collection.add_book_in_favorites('Книга 2 Ужасы')
        test_collection.delete_book_from_favorites('Книга 1 Фантастика')
        assert test_collection.favorites == ['Книга 2 Ужасы']

    def test_get_list_of_favorites_books_add_3_books_receive_list_of_3(self, test_collection):
        test_collection.add_book_in_favorites('Книга 1 Фантастика')
        test_collection.add_book_in_favorites('Книга 2 Ужасы')
        test_collection.add_book_in_favorites('Книга 7 без жанра')
        assert test_collection.get_list_of_favorites_books() == ['Книга 1 Фантастика', 'Книга 2 Ужасы', 'Книга 7 без жанра']

