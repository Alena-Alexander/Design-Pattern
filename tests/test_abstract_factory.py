from src.Creational.abstract_factory import SkullShirt, FlowerShirt
import unittest


class TestAbstractFactory(unittest.TestCase):
    def test_skull_shirt(self):
        skull_shirt = SkullShirt()

    def test_flower_shirt(self):
        flower_shirt = FlowerShirt()
