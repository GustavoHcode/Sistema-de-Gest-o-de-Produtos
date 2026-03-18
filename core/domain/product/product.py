class Product:
    def __init__(self, name: str, amount: int, price_sale: float , price_buy: float):
        self.name = name 
        self.price_sale = price_sale 
        self.price_buy = price_buy
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.price_buy}, {self.price_sale}, {self.amount}"
        