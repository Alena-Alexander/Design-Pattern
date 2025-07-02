from datetime import date
import pytest
import unittest
from src.Creational.lazy_init import Person


class TestLazyInit(unittest.TestCase):

    def test_lazy_init(self):
        person = Person("Alena", date(2004, 9, 4))
        assert person.name == "Alena"
        assert person.age == "21"
        print(f"{person}")


if __name__ == "__main__":
    pytest.main(["-v"])
