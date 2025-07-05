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
        """
        Must display the color of the skull shirt.

        :return: str
        """
        return self._color

    def shirt_material(self):
        """
        Must display the skull shirts material.

        :return: str
        """
        return self._material


class FlowerShirt(ShirtFactory):
    def __init__(self):
        self._color = "Black"
        self._material = "Silk"

    def shirt_color(self):
        """
        Must display the color of the flower shirt.

        :return: str
        """
        return self._color

    def shirt_material(self):
        """
        Must display the flower shirts material.

        :return: str
        """
        return self._material


def main():
    """
    As long as this while loop is True the program will ask the user to "Choose a shirt between the Skull shirt,
    and Flower shirt, to identify "the materials of it" and if the shirt chosen is within the two options given then
    the loop will break, ignore the else statement and move on to the code below.

    :return: str
    """
    while True:
        shirt_chosen = input("Choose a shirt between the Skull shirt, and Flower shirt, to identify "
                             "the materials of it")

        if shirt_chosen in ["Skull shirt", "Flower shirt"]:
            break
        else:
            print("invalid option was chosen...")

    """
    The code below identifies the variables skull_shirt and flower_shirt as type SkullShirt, and FlowerShirt, allowing
    you to use those classes methods and such. And if the shirt chosen by the user is "Skull shirt", then an instance of
    the SkullShirt class is created, else if the shirt chosen by the user is "Flower shirt", then an instance of
    the FlowerShirt class is created. And then then the methods for the classes are ran.
    """
    skull_shirt: SkullShirt
    flower_shirt: FlowerShirt

    if shirt_chosen == "Skull shirt":
        skull_shirt = SkullShirt()
    elif shirt_chosen == "Flower shirt":
        flower_shirt = FlowerShirt()
    else:
        print("Meh...")

    skull_shirt.shirt_material()
    flower_shirt.shirt_material()

    skull_shirt.shirt_color()
    flower_shirt.shirt_color()


if __name__ == "__main__":
    main()
