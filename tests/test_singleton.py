from src.Creational.singleton import Logger
import unittest


class TestSingleton(unittest.TestCase):
    """
    This test is meant to test the functionality of my Singleton class
    using the unittest framework and inheriting from its TestCase class to
    organize and provide structure for this unit test.

    This test includes assertions which are debugging tools used to help
    the flow of code. They're mainly assumption that the programmer knows
    or wants to be true, and if the there not truer than they don't allow
    the code to execute.(In short assertion is a boolean expression that
    checks if a statement is True or False).

    assertEqual, assertTrue, assertRaises, assert are 4 examples of
    assertion.
    """

    def test_singleton(self):
        logger1 = Logger()
        logger2 = Logger()

        logger1.log("Hi")
        logger2.log("Hello")

        self.assertIs(logger1, logger2, "logger1 and logger2 are not a part of"
                                        "the same object")

        print("There's only one instance")


if __name__ == "__main__":
    unittest.main()
