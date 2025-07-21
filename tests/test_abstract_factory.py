from src.Creational.abstract_factory import ShirtFactory, SkullShirt, FlowerShirt
import unittest
from abc import ABC


class TestAbstractFactory(unittest.TestCase):
    """
    This test uses the assert methods assertEqual to test if the material
    and color for each shirt are equal to what they need to be, and the
    assertIsInstance method to test both concrete class(SkullShirt, FlowerShirt)
    are instances of the abstract class(ShirtFactory).
    """

    def test_skull_shirt(self):
        skull_shirt = SkullShirt()
        self.assertIsInstance(skull_shirt, ShirtFactory, "SkullShirt is not an instance of the ShirtFactory class")
        self.assertEqual(skull_shirt.shirt_color(), "White", "The Skull shirts color is not equal to White")
        self.assertEqual(skull_shirt.shirt_material(), "Cotton", "The Skull shirts material is not equal to Cotton")

    def test_flower_shirt(self):
        flower_shirt = FlowerShirt()
        self.assertIsInstance(flower_shirt, ShirtFactory, "FlowerShirt is not an instance of the ShirtFactory class")
        self.assertEqual(flower_shirt.shirt_color(), "Black", "The Flower shirts color is not equal to Black")
        self.assertEqual(flower_shirt.shirt_material(), "Silk", "The Flower shirts material is not equal to Silk")
