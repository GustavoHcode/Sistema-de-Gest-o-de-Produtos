class Product:
    def __init__(self, id, name: str, amount: int, sale_price: float , buy_price: float):
        self.id = id
        self.name = name 
        self.sale_price = sale_price 
        self.buy_price = buy_price
        self.amount = amount

    def __str__(self):
        return f"{self.name}, {self.price_buy}, {self.price_sale}, {self.amount}"
        