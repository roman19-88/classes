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
# Продукты магазина

## Классы

### Smartphone
Наследуется от Product.
- Атрибуты:
- efficiency: Производительность.
- model: Модель.
- memory: Объем памяти.
- color: Цвет.

### LawnGrass
Наследуется от Product.
- Атрибуты:
- country: Страна-производитель.
- germination_period: Срок прорастания.
- color: Цвет.

## Mixin
Класс-миксин добавляет побочный эффект при инициализации: печатает имя класса и переданные аргументы конструктора.

- **Расположение**: `src/product.py` (`class Mixin`)
- **Поведение**: при создании экземпляров `Product`, `Smartphone`, `LawnGrass` вызывается `print(self.__class__.__name__, args)` внутри `Mixin.__init__`.

### Пример
```python
from src.product import Product

p = Product("Телефон", "Смартфон", 20000, 10)
# Консоль:
# Product ('Телефон', 'Смартфон', 20000, 10)
```

## Тестирование
Проект использует `pytest`.

- Запуск тестов:
```bash
pytest -q
```

В том числе добавлены тесты для проверки работы миксина: `tests/test_mixin.py`.