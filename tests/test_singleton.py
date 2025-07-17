from src.Creational.singleton import SingletonOne
import unittest
import pytest


class TestSingleton(type, unittest.TestCase):
    """
    Inherits from type allowing you to modify the blueprint of the class, and thus making it a metaclass.
    The built-in type metaclass is used for creating all classes in python, and is used to override its
    methods __new__ & __init__.
    """
    _instances = {}  # Where that metaclass instance will be maintained

    def __call__(cls, *args, **kwargs):  # cls: represents the class itself, *args: tuple,**kwargs: dictionary
        """

        The __call__ method is a static method that gives access to the instance of the class and call the instance
        and can only be accessed from inside the class, due to the private access modifier (__method__). its main purpose
        is to write a class and call a function.

        :param args: tuple
        :param kwargs: dict[str, any]
        :return: cls._instances
        """
        if cls not in cls._instances:  # If there's not an instance in this class inside the instance dictionary(_instances)
            cls._instances[cls] = super(TestSingleton, cls).__call__(*args,
                                                                     **kwargs)  # we create the instance of the class
        return cls._instances[cls]  # else we return the instance


class Logger(metaclass=TestSingleton, unittest.TestCase):
    def test_log(self, msg):
        print(msg)


if __name__ == "__main__":
    logger = Logger()
    logger2 = Logger()
    print(logger)
    print(logger2)
    logger.test_log("Hello")
    logger.test_log("Hi..")
