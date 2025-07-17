class Shirt:
    def __init__(self, shirt_size: str, sleeve_length: int, shirt_material: str):
        """
        The Class represents the most basic aspects of a shirt.

        :param shirt_size: The size of a shirt.
        :param sleeve_length: The length of the sleeve.
        :param shirt_material: The material the shirts made out of.
        """
        self._shirt_size = shirt_size
        self._sleeve_length = sleeve_length
        self._shirt_material = shirt_material

    def get_shirt_size(self):
        """
        Return the size of a shirt.

        :return: str
        """
        return self._shirt_size

    def get_sleeve_length(self):
        """
        Returns the length of a shirts sleeve.

        :return: int
        """
        return self._sleeve_length

    def get_shirt_material(self):
        """
        Returns the material of a shirt.

        :return: int
        """
        return self._shirt_material
