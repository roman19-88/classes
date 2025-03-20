## Классы

### Product
Класс для создания продукта.

- Атрибуты:
- name: название (строка)
- description: описание (строка)
- price: цена (float)
- quantity: количество (int или str)

### Category
Класс для создания категории продуктов.

- Атрибуты:
- name: название (строка)
- description: описание (строка)
- products: список объектов Product
- category_count: общее количество категорий (статический)
- product_count: общее количество продуктов (статический)

## Пример использования


from your_module import Product, Category  # Замените на правильный импорт

product1 = Product("Товар 1", "Описание товара 1", 10.99, 5)
product2 = Product("Товар 2", "Описание товара 2", 15.50, "10")
category = Category("Категория 1", "Описание категории 1", [product1, product2])

print(f"Категорий: {Category.category_count}, Продуктов: {Category.product_count}")


## Тестирование

Запустите тесты с помощью
unittest