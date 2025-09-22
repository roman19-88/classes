from abc import ABC, abstractmethod
from typing import Union


class BaseProduct(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_info):
        pass


class Mixin:
    def __init__(self, *args) -> None:
        print(self.__class__.__name__, args)


class Product(Mixin, BaseProduct):
    name: str
    description: str
    quantity: Union[int, str]

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
    super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_info):
        name = product_info.get("name")
        price = product_info.get("price")
        description = product_info.get("description")
        quantity = product_info.get("quantity")
        return cls(name, description, price, quantity)


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
