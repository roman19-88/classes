import pytest

from src.main import Category, Product


@pytest.fixture
def setup_products():
    """Fixture для создания тестовых продуктов и категории."""
    banana = Product('Banana', 'Fresh bananas', 10.0, 50)
    apple = Product('Apple', 'Juicy apples', 5.0, 30)
    fruits_category = Category('Fruits', 'Mixed fruits', [banana])
    return banana, apple, fruits_category


def test_product_initialization(setup_products):
    """Тест на инициализацию класса Product."""
    banana, apple, _ = setup_products
    assert banana.name == 'Banana'
    assert banana.description == 'Fresh bananas'
    assert banana.get_price == 10.0
    assert banana.quantity == 50


def test_product_price_update(setup_products):
    """Тест на обновление цены продукта."""
    banana, _, _ = setup_products
    banana.get_price = 12.0
    assert banana.get_price == 12.0


def test_product_price_should_not_be_negative(capfd, setup_products):
    """Тест, чтобы убедиться, что цена не может быть отрицательной."""
    banana, _, _ = setup_products
    banana.get_price = -5  # Это вызовет сообщение
    captured = capfd.readouterr()  # Захватываем вывод
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_add_product_to_category(setup_products):
    """Тест добавления продукта в категорию."""
    banana, apple, fruits_category = setup_products
    fruits_category.add_product(apple)

    # Проверяем, что продукты добавлены
    assert len(fruits_category.products) == 2
    assert fruits_category.products[0] == 'Banana, 10.0 руб. Остаток: 50 шт.'
    assert fruits_category.products[1] == 'Apple, 5.0 руб. Остаток: 30 шт.'


def test_category_product_count(setup_products):
    """Тест на количество продуктов в категории."""
    banana, apple, fruits_category = setup_products
    fruits_category.add_product(apple)
    assert Category.product_count == 1
