import pytest
from main import BooksCollector


@pytest.fixture
def test_collection():
    test_collection = BooksCollector()
    test_collection.add_new_book('Книга 1 Фантастика')
    test_collection.add_new_book('Книга 2 Ужасы')
    test_collection.add_new_book('Книга 3 Детективы')
    test_collection.add_new_book('Книга 4 Мультфильмы')
    test_collection.add_new_book('Книга 5 Комедии')
    test_collection.add_new_book('Книга 6 Ужасы')
    test_collection.add_new_book('Книга 7 без жанра')
    test_collection.set_book_genre('Книга 1 Фантастика', 'Фантастика')
    test_collection.set_book_genre('Книга 2 Ужасы', 'Ужасы')
    test_collection.set_book_genre('Книга 3 Детективы', 'Детективы')
    test_collection.set_book_genre('Книга 4 Мультфильмы', 'Мультфильмы')
    test_collection.set_book_genre('Книга 5 Комедии', 'Комедии')
    test_collection.set_book_genre('Книга 6 Ужасы', 'Ужасы')
    return test_collection
