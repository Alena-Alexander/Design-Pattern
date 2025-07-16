"""
Singleton relies on two mechanisms of object orientation:
    1. A static method or class method that gives access to the instance of the class.
    2. A private access modifier that allows access to a method only from inside the class.

By making the constructor private only the static method inside the class can create an instance,
so the class has full control over what can control the instance.
"""


class SingletonOne(type):
    """
    Inherits from the type class allowing you to modify the blueprint of said class using the __call__ method
    making it a metaclass.

    Type is a metaclass used to modify all classes in Python.
    """
    _instances = {}  # A dict that is used to contain the instance of the class

    def __call__(cls, *args, **kwargs):
        """
        Gives you access to the class and its instance, it includes an if statements that checks in the
        instance has been created and if it hasn't it do so, else it'll return that instance.


        :param args: tuple[Any, ...]
        :param kwargs: dict[str, Any]
        :return: cls._instances
        """
        if cls not in cls._instances:  # If there are no instances in cls._instances
            cls._instances[cls] = super(SingletonOne, cls).__call__(*args, **kwargs)  # Uses the super method to refer
            # to the parent class(SingletonOne) and use its method __call__.
        return cls._instances[cls]


class Logger(metaclass=SingletonOne):
    """
    Inherits from the SingletonOne class allowing there to only be one instance of a class.
    """

    def log(self, msg):
        """
        Prints a message
        :param msg: str      :
        """
        print(msg)


if __name__ == "__main__":
    Logger = Logger()
    print(Logger)
    Logger.log("Sup")
