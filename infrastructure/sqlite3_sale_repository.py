import sqlite3
from datetime import datetime
from domain.sale.sale_interface import InterfaceSale
from domain.sale.sale import Sale

class SQLiteSaleRepository(InterfaceSale):
    def __init__(self, db_path="DistribDB.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sale (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT NOT NULL);""")
        self.conn.commit()

    def save(self, sale: Sale):

        product_id = sale.product_id
        quantity = sale.quantity
        

        self.cursor.execute("SELECT amount, sale_price FROM product WHERE id = ?", (product_id,))
        product = self.cursor.fetchone()

        if product is None:
            print("Produto não existe")
            self.conn.close()
            return False
        
        stock, price = product

        if stock < quantity:
            print("Estoque insuficiente")
            return
        
        self.cursor.execute("INSERT INTO sale (date) VALUES (?)",
                            (datetime.now().strftime("%Y-%m-%d"),)
                            )
        
        sale_id = self.cursor.lastrowid

        self.cursor.execute(
            "INSERT INTO sale_item (sale_id, product_id, quantity, price) VALUES (?,?,?,?)",
            (sale_id, product_id, quantity, price)
        )

        self.cursor.execute(
            "UPDATE product SET amount = amount - ? WHERE id = ?",
            (quantity, product_id)
        )

        self.conn.commit()
        