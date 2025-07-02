from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from dataclasses import dataclass
from functools import wraps
from typing import Optional, TypeVar, Type, Any

T = TypeVar('T')


def enforce_return_type(return_type: Type[T]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            result = func(*args, **kwargs)
            if not isinstance(result, return_type):
                raise TypeError(f"Function {func.__name__} should return type {return_type.__name__}, but returned type {type(result).__name__}")
            return result
        return wrapper
    return decorator


# Interface class Fruit: No implemented functions, but they describe the structure
# of the family or group objects. Declares the operations that all concrete fruit
# must implement.
class IFruit(ABC):

    @abstractmethod
    def shape(self):
        raise NotImplementedError("Must implement function shape")

    @abstractmethod
    def color(self):
        raise NotImplementedError("Must implement function color")


# Abstract class Apple: partially implemented class, but it describes the structure
# of the subset for the family or group of objects
@dataclass
class Apple(IFruit):
    _shape: Optional[str] = None

    def __init__(self):
        self._shape = "Round"

    def shape(self):
        return self._shape

    @abstractmethod
    def color(self):
        raise NotImplementedError("Must implement the color of the apple")


# Concrete Class Macintosh: fully implemented class, describes the actual object itself
@dataclass
class Macintosh(Apple):
    _color: Optional[str] = None

    def __init__(self):
        super().__init__()
        self._color = "Redish/Green"

    def color(self):
        return self._color


# Concrete Class Macintosh: fully implemented class, describes the actual object itself
@dataclass
class Fuji(Apple):
    _color: Optional[str] = None

    def __init__(self):
        super().__init__()
        self._color = "Redish"

    def color(self):
        self._color = "Redish"
        return self._color


@dataclass
class Grape(IFruit):
    _shape: Optional[str] = None

    def __init__(self):
        self._shape = "Round"

    def shape(self):
        return self._shape

    @abstractmethod
    def color(self):
        raise NotImplementedError("Must implement the color of grape")


@dataclass
class Concord(Grape):
    _color: Optional[str] = None

    def __init__(self):
        super().__init__()
        self._color = "Purple"

    def color(self):
        return self._color


@dataclass
class Dominga(Grape):
    _color: Optional[str] = None

    def __init__(self):
        super().__init__()
        self._color = "Green"

    def color(self):
        return self._color


# Abstract Fruit Factory Class
class AbstractFruitFactory(ABC):

    @staticmethod
    @abstractmethod
    @enforce_return_type(IFruit)
    def create_fruit(name: str) -> IFruit:
        raise NotImplementedError("Must implement the type of fruit")


# Abstract Apple Factory Class
class AppleFactory(AbstractFruitFactory):

    @staticmethod    # static method/function
    @enforce_return_type(IFruit)
    def create_fruit(name: str) -> IFruit:
        if name.lower() == "macintosh":
            return Macintosh()
        elif name.lower() == "fuji":
            return Fuji()


class GrapeFactory(AbstractFruitFactory):

    @staticmethod    # static method/function
    @enforce_return_type(IFruit)
    def create_fruit(name: str) -> IFruit:
        if name.lower() == "concord":
            return Concord()
        elif name.lower() == "dominga":
            return Dominga()


if __name__ == "__main__":
    macintosh = AppleFactory.create_fruit("fuji")
    print(macintosh)

    dominga = GrapeFactory.create_fruit("dominga")
    print(dominga)