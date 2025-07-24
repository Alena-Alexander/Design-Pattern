from src.Creational.factory import Shirt, FlowerShirt, SkullShirt
import unittest


class TestFactoryMethod(unittest.TestCase):
    def test_shirts_initialization_nmethods(self):
        shirt_ = Shirt(10, "Yellow", "Linen")
        self.assertEqual(shirt_.get_shirt_size(), 10, "The shirt size isn't equal to 10")
        self.assertEqual(shirt_.get_shirt_color(), "Yellow", "The shirts color is not equal to Yellow")
        self.assertEqual(shirt_.get_shirt_material(), "Linen", "The shirts material is not equal to Linen")

        flower_shirt = FlowerShirt(8, "Black", "Silk", "Red/Pink/White/nBeegSpinalcord")
        self.assertEqual(flower_shirt.get_shirt_size(), 8, "The flower shirt size isn't equal to 8")
        self.assertEqual(flower_shirt.get_shirt_color(), "Black", "The flower shirt color isn't equal to Black")
        self.assertEqual(flower_shirt.get_shirt_material(), "Silk", "The flower shirts material is not equal to Silk")
        self.assertEqual(flower_shirt.get_flower_shirt_flower_features(), "Red/Pink/White/nBeegSpinalcord")

        skull_shirt = SkullShirt(11, "White", "Cotton", "Tan/LightBrown/MushroomnSticks")
        self.assertEqual(skull_shirt.get_shirt_size(), 11, "The skull shirt size isn't equal to 11")
        self.assertEqual(skull_shirt.get_shirt_color(), "White", "The Skull shirts color is not equal to White")
        self.assertEqual(skull_shirt.get_shirt_material(), "Cotton", "The Skull shirts material is not equal to Cotton")
        self.assertEqual(skull_shirt.get_skull_shirt_skull_features(), "Tan/LightBrown/MushroomnSticks")


if __name__ == "__main__":
    unittest.main()
