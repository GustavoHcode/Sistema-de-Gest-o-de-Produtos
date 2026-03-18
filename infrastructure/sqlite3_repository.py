import sqlite3
from core.domain.product.product_interface import InterfaceProduct
from core.domain.product.product import Product

class SQLiteProductRepository(InterfaceProduct):
    def __init__(self, db_path="DistribDB.db"):
        self.conn = sqlite3.connect(db_path,
                                    check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS product(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL, 
                            amount INT NOT NULL, 
                            sale_price FLOAT NOT NULL, 
                            buy_price FLOAT NOT NULL)""")
        self.conn.commit()

    def save(self, product: Product):
        self.cursor.execute(
            "INSERT INTO product (name, amount, sale_price, buy_price) VALUES (?, ?, ?, ?)",
            (product.name, product.amount, product.sale_price, product.buy_price)
        )
        self.conn.commit()

    def remove(self, product_id):
        self.cursor.execute(
            "DELETE FROM product WHERE id = ? ",
            (product_id,)
        )
        self.conn.commit()            
        
    
    def list(self):
        self.cursor.execute("SELECT id, name, amount, sale_price, buy_price FROM product",)
        rows = self.cursor.fetchall()
        return rows
    
    def edit(self, product: Product):
        self.cursor.execute("""
            UPDATE product SET name = ?, amount = ?, sale_price = ?, buy_price = ? WHERE id = ?""", 
            (product.name, product.amount, product.sale_price, product.buy_price, product.id ))
        self.conn.commit()   