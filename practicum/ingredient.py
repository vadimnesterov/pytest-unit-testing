class Ingredient:
    """
    Model of a burger ingredient.
    An ingredient is either a filling or a sauce.
    It has a type, a name, and a price.
    """

    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type
