from src.product import Product
import pytest


def test_product_initialization():
    product = Product("Телефон", "Смартфон с хорошей камерой", 20000, 10)

    assert product.name == "Телефон"
    assert product.description == "Смартфон с хорошей камерой"
    assert product.price == 20000
    assert product.quantity == 10


def test_price_setter_and_getter():
    product = Product("Телефон", "Смартфон с хорошей камерой", 20000, 10)

    # Проверка установки положительной цены
    product.price = 25000
    assert product.price == 25000

    # Проверка попытки установки отрицательной цены
    product.price = -5000  # Это должно вывести сообщение, но цена не должна измениться
    assert product.price == 25000  # Цена должна остаться 25000

    # Проверка попытки установки нулевой цены
    product.price = 0  # Это должно вывести сообщение
    assert product.price == 25000  # Цена все еще должна оставаться 25000


def test_new_product_class_method():
    product_info = {
        "name": "Ноутбук",
        "description": "Мощный ноутбук для работы",
        "price": 50000,
        "quantity": 5,
    }
    product = Product.new_product(product_info)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный ноутбук для работы"
    assert product.price == 50000
    assert product.quantity == 5


@pytest.fixture
def product1():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_add_method(product1, product2):
    # Ожидаемая стоимость: (210000.0 * 8) + (31000.0 * 14)
    expected_total_price = (210000.0 * 8) + (31000.0 * 14)
    assert product1 + product2 == expected_total_price


def test_str_method(product1):
    expected_str = 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'
    assert str(product1) == expected_str


def test_zero_quantity_raises_value_error():
    """Тест проверяет, что создание товара с нулевым количеством вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Телефон", "Смартфон с хорошей камерой", 20000, 0)
