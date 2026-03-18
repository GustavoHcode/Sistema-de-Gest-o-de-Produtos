from core.domain.product.product_interface import InterfaceProduct
from core.domain.product.product import Product
class CreateProduct:
    def __init__(self, repository: InterfaceProduct):
        self.repository = repository
        
    def execute(self, data):
        new_product = Product(

            name=data['name'],
            amount=data['amount'],
            price_sale=data['sale_price'],
            price_buy=data['sale_buy'])
        
        self.repository.save(new_product)
        return new_product

class RemoveProduct:
    def __init__(self, repository: InterfaceProduct):
        self.repository = repository

    def execute(self, product_id):
        self.repository.remove(product_id)

class ListProduct:
    def __init__(self, repository: InterfaceProduct):
        self.repository = repository

    def execute(self):
        dados = self.repository.list()   
        return  dados 

class EditProduct:
    def __init__(self, repository: InterfaceProduct):
        self.repository = repository

    def execute(self, product):
        self.repository.edit(product)    
            