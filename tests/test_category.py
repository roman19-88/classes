from src.category import Category
from src.product import Product
import pytest


# Тесты для класса Category
def test_category_initialization():
    category = Category("Электроника", "Все о электронике.", [])

    assert category.name == "Электроника"
    assert category.description == "Все о электронике."
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product():
    category = Category("Электроника", "Все о электронике.", [])
    product1 = Product("Телефон", "Электроника", 20000, 10)

    category.add_product(product1)

    assert len(category.products) == 1
    assert category.products[0] == "Телефон, 20000 руб. Остаток: 10 шт."
    assert Category.product_count == 1

    product2 = Product("Ноутбук", "Электроника", 50000, 5)
    category.add_product(product2)

    assert len(category.products) == 2
    assert category.products[1] == "Ноутбук, 50000 руб. Остаток: 5 шт."
    assert Category.product_count == 2


def test_products_property():
    category = Category("Электроника", "Все о электронике.", [])
    product1 = Product("Телефон", "Электроника", 20000, 10)
    product2 = Product("Ноутбук", "Электроника", 50000, 5)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = [
        "Телефон, 20000 руб. Остаток: 10 шт.",
        "Ноутбук, 50000 руб. Остаток: 5 шт.",
    ]
    assert category.products == expected_output


@pytest.fixture
def product1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category(product1, product2):
    # Создаем категорию с двумя продуктами
    return Category("Смартфоны", "Мобильные телефоны", [product1, product2])


def test_str_method(category):
    # Ожидаемая строка: название категории и общее количество продуктов
    expected_str = "Смартфоны, количество продуктов: 22 шт."  # 8 (Iphone) + 14 (Xiaomi)
    assert str(category) == expected_str


def test_average_price_with_products(category):
    """Тест проверяет корректный расчет среднего ценника для категории с товарами"""
    # Средняя цена: (210000.0 + 31000.0) / 2 = 120500.0
    expected_average = (210000.0 + 31000.0) / 2
    assert category.average_price() == expected_average


def test_average_price_empty_category():
    """Тест проверяет, что для пустой категории возвращается 0"""
    empty_category = Category("Пустая категория", "Категория без товаров", [])
    assert empty_category.average_price() == 0


def test_average_price_single_product():
    """Тест проверяет расчет среднего ценника для категории с одним товаром"""
    product = Product("Телефон", "Смартфон", 50000, 1)
    category = Category("Электроника", "Категория с одним товаром", [product])
    assert category.average_price() == 50000
