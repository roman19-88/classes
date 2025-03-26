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
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_info):
        name = product_info.get("name")
        price = product_info.get("price")
        description = product_info.get("description")
        quantity = product_info.get("quantity")
        return cls(name, description, price, quantity)
