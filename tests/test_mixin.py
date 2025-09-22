import builtins
import pytest

from src.product import Product, Smartphone, LawnGrass


@pytest.mark.parametrize(
    "factory,args,kwargs,expected_class_name",
    [
        (Product, ("Телефон", "Смартфон", 1000.0, 2), {}, "Product"),
        (
            Smartphone,
            ("S23", "256GB", 180000.0, 5, 95.5, "S23", 256, "Gray"),
            {},
            "Smartphone",
        ),
        (
            LawnGrass,
            ("Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зелёный"),
            {},
            "LawnGrass",
        ),
    ],
)

def test_mixin_prints_class_name_and_args(factory, args, kwargs, expected_class_name, monkeypatch):
    printed = []

    def fake_print(*values, **k):
        printed.append(" ".join(str(v) for v in values))

    monkeypatch.setattr(builtins, "print", fake_print)

    obj = factory(*args, **kwargs)
    assert obj

    assert printed
    first_line = printed[0]
    assert expected_class_name in first_line
    for value in args[:3]:
        assert str(value) in first_line
