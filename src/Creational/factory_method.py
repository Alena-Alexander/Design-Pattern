"""

"""

from abc import ABC, abstractmethod


class ShirtFactory(ABC):
    """
    The class represents a blueprint for a shirts material and color.

    It contains to methods that are meant to inherited.
    """

    @abstractmethod
    def shirt_color(self):
        """
        Must display the color of the shirt.

        :return: str
        """

    @abstractmethod
    def shirt_material(self):
        """
        Must display the shirts material.

        :return: str
        """


class SkullShirt(ShirtFactory):
    """
    Describes the color and material of a Skull shirt.
    """

    def __init__(self):
        self._color = "White"
        self._material = "Cotton"

    def shirt_color(self):
        return self._color

    def shirt_material(self):
        return self._material


class FlowerShirt(ShirtFactory):
    def __init__(self):
        self._color = "Black"
        self._material = "Silk"

    def shirt_color(self):
        return self._color

    def shirt_material(self):
        return self._material


