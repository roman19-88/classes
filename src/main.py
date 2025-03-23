from typing import Union


class Product:
    name: str
    description: str
    price: Union[float, int]
    quantity: Union[int, str]

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_info):
        name = product_info.get('name')
        price = product_info.get('price')
        description = product_info.get('description')
        quantity = product_info.get('quantity')
        return cls(name, description, price, quantity)


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

    @property
    def products(self):
        return [f"{el.name}, {el.get_price} руб. Остаток: {el.quantity} шт." for el in self.__products]
