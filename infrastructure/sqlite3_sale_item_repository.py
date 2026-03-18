import sqlite3


class SQLiteSaleItemRepository:
    def __init__(self, db_path="DistribDB.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sale_item (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                sale_id INTEGER,
                                product_id INTEGER,
                                quantity INTEGER,
                                price REAL,
                                FOREIGN KEY(sale_id) REFERENCES sale(id),
                                FOREIGN KEY(product_id) REFERENCES product(id));""")
        self.conn.commit()    