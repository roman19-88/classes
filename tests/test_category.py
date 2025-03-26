from src.category import Category
from src.product import Product


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
