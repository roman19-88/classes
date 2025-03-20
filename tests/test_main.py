import unittest

from src.main import Category, Product


def test_product_initialization():
    """Проверка инициализации объекта Product"""
    product = Product("Товар 1", "Описание товара 1", 10.99, 5)
    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 10.99
    assert product.quantity == 5


def test_product_with_string_quantity():
    """Проверка инициализации объекта Product с количествo как строка"""
    product = Product("Товар 2", "Описание товара 2", 15.50, "10")
    assert product.quantity == "10"


def test_category_initialization():
    """Проверка инициализации объекта Category"""
    product1 = Product("Товар 1", "Описание товара 1", 10.99, 5)
    product2 = Product("Товар 2", "Описание товара 2", 15.50, "10")
    category = Category("Категория 1", "Описание категории 1", [product1, product2])

    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert len(category.products) == 2
    assert product1 in category.products
    assert product2 in category.products


def reset_category_and_product_counts():
    """ Сброс значений счетчиков категорий и продуктов """
    Category.category_count = 0
    Category.product_count = 0


def test_static_category_count():
    """ Проверка счетчика категорий """

    reset_category_and_product_counts()  # Сбрасываем счетчики перед тестом
    product1 = Product("Товар 1", "Описание товара 1", 10.99, 5)
    product2 = Product("Товар 2", "Описание товара 2", 15.50, "10")
    category = Category("Категория 1", "Описание категории 1", [product1, product2])

    assert Category.category_count == 1


def test_static_product_count():
    """ Проверка счетчика продуктов """
    reset_category_and_product_counts()
    product1 = Product("Товар 1", "Описание товара 1", 10.99, 5)
    new_category = Category("Категория 1", "Описание категории 1", [product1])

    assert Category.product_count == 1  # Должно быть 1 после создания первой категории с продуктом

    new_product = Product("Товар 2", "Описание товара 2", 15.50, 3)
    new_category_2 = Category("Категория 2", "Описание категории 2", [new_product])

    assert Category.product_count == 2  # Должно быть 2 после создания второй категории с продуктами


if __name__ == "__main__":
    unittest.main()
