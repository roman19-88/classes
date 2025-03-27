from typing import Union


class Category:
    name: str
    description: str
    products: Union[list, None]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"{el.name}, {el.price} руб. Остаток: {el.quantity} шт."
            for el in self.__products
        ]
