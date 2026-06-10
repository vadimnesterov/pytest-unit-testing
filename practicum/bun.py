class Bun:
    """
    Model of a burger bun.
    A bun has a name and a price.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
