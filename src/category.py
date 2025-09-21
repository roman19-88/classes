from typing import Union

from .product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self):
        total_quantity = sum([x.quantity for x in self.__products])
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return [
            f"{el.name}, {el.price} руб. Остаток: {el.quantity} шт."
            for el in self.__products
        ]

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    def average_price(self):
        try:
            if len(self.__products) == 0:
                return 0
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


