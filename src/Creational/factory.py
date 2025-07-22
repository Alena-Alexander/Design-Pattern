class Shirt:
    def __init__(self, size: int, color: str, material: str):
        """
        The Class represents the most basic aspects of a shirt.

        :param size: The size of a shirt.
        :param color: The color of the shirt.
        :param material: The material the shirts made out of.
        """
        self._size = size
        self._color = color
        self._material = material

    def get_shirt_size(self):
        """
        Return the size of a shirt.

        :return: int
        """
        return self._size

    def get_shirt_color(self):
        """
        Returns the color of the shirt.

        :return: str
        """
        return self._color

    def get_shirt_material(self):
        """
        Returns the material of a shirt.

        :return: str
        """
        return self._material


class FlowerShirt(Shirt):
    """
    The Class represents the most basic aspects of a Flower shirt.

    :param size: The size of a shirt.
    :param color: The color of the shirt.
    :param material: The material the shirts made out of.
    :param flower: The flower features.
    """

    def __init__(self, size: int, color: str, material: str, flower: str):
        """
        Initializes the features of the Flower shirt.

        :param size: The size of a shirt.
        :param color: The color of the shirt.
        :param material: The material the shirts made out of.
        :param flower: The flower features.
        """
        Shirt.__init__(self, size, color, material)

        self._flower = flower

    def get_shirt_size(self):
        """
        Return the size of a shirt.

        :return: int
        """
        return self._size

    def get_shirt_color(self):
        """
        Returns the color of the shirt.

        :return: str
        """
        return self._color

    def get_shirt_material(self):
        """
        Returns the material of a shirt.

        :return: str
        """
        return self._material

    def get_flower_shirt_flower_features(self):
        """
        Returns the features of the flower design on the shirt.

        :return: str
        """
        return self._flower

class SkullShirt(Shirt):
    """
    The Class represents the most basic aspects of a Skull shirt.

    :param size: The size of a shirt.
    :param color: The color of the shirt.
    :param material: The material the shirts made out of.
    :param skull: The skull features.
    """

    def __init__(self, size: int, color: str, material: str, skull: str):
        """
        Initializes the features of the Flower shirt.

        :param size: The size of a shirt.
        :param color: The color of the shirt.
        :param material: The material the shirts made out of.
        :param skull: The skull features.
        """
        Shirt.__init__(self, size, color, material)

        self._skull = skull

    def get_shirt_size(self):
        """
        Return the size of a shirt.

        :return: int
        """
        return self._size

    def get_shirt_color(self):
        """
        Returns the color of the shirt.

        :return: str
        """
        return self._color

    def get_shirt_material(self):
        """
        Returns the material of a shirt.

        :return: str
        """
        return self._material

    def get_skull_shirt_skull_features(self):
        """
        Returns the features of the skull design on the shirt.

        :return: str
        """
        return self._skull


if __name__ == "__main__":
    skull_shirt = SkullShirt(11, "White", "Cotton", "Tan/LightBrown/MushroomnSticks")
    flower_shirt = FlowerShirt(8, "Black", "Silk", "Red/Pink/White/nBeegSpinalcord")
    print("The following describes the skull shirt")
    print("Skull shirt size: ", skull_shirt.get_shirt_size())
    print("Skull shirt color: ", skull_shirt.get_shirt_color())
    print("Skull shirt material: ", skull_shirt.get_shirt_material())
    print("SkullFeatures: ", skull_shirt.get_skull_shirt_skull_features())

    print("The following describes a flower shirt")
    print("Flower shirt size: ", flower_shirt.get_shirt_size())
    print("Flower shirt color: ", flower_shirt.get_shirt_color())
    print("Flower shirt material: ", flower_shirt.get_shirt_material())
    print("FlowerFeatures: ", flower_shirt.get_flower_shirt_flower_features())
