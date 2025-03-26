import pytest
from src.category import Category

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
