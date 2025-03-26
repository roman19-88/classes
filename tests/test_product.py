import pytest
from src.product import Product
from src.category import Category



def test_product_price_should_not_be_negative(capfd, setup_products):
    """Тест, чтобы убедиться, что цена не может быть отрицательной."""
    banana, _, _ = setup_products
    banana.get_price = -5  # Это вызовет сообщение
    captured = capfd.readouterr()  # Захватываем вывод
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
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
    assert banana.price == 10.0
    assert banana.quantity == 50
def test_product_price_update(setup_products):
    """Тест на обновление цены продукта."""
    banana, _, _ = setup_products
    banana.price = 12.0
    assert banana.price == 12.0
