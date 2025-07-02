from src.Creational import fruit


def client(factory: fruit.AbstractFruitFactory) -> fruit.AbstractFruitFactory:
    print(f"Creating {factory.__name__} factory")
    return factory()


if __name__ == "__main__":
    grape_factory = client(fruit.GrapeFactory)
    dominga = grape_factory.create_fruit("dominga")
    print(dominga)
