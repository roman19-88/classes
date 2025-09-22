from src.category import Category
from src.product import LawnGrass, Smartphone
import pytest


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def smartphone3():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


def test_smartphone_initialization(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_lawngrass_initialization(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == (180000.0 * 5) + (210000.0 * 8)


def test_lawngrass_add(grass1, grass2):
    assert grass1 + grass2 == (500.0 * 20) + (450.0 * 15)


def test_add_different_types_raises_type_error(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_category_add_smartphone(smartphone1, smartphone2, smartphone3):
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_smartphones.add_product(smartphone3)
    assert len(category_smartphones.products) == 3
    assert (
        category_smartphones.products[2]
        == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_category_add_lawngrass(grass1, grass2):
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1]
    )
    category_grass.add_product(grass2)
    assert len(category_grass.products) == 2
    assert category_grass.products[1] == "Газонная трава 2, 450.0 руб. Остаток: 15 шт."


@pytest.fixture
def category_smartphones(smartphone1, smartphone2):
    return Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )


def test_category_add_non_product_raises_type_error(category_smartphones):
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")

