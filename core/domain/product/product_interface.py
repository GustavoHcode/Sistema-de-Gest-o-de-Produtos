from abc import ABC, abstractmethod

class InterfaceProduct(ABC): 
    
    @abstractmethod
    def save(self, product): 
        pass 

    def remove(self, product_id):
        pass 

    def list(self, product):
        pass 
    
    def edit(self, product):
        pass 
