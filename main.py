from flask import Flask 
from infrastructure.sqlite3_repository import SQLiteProductRepository
from core.use_case.product_use_case.product_use_case import CreateProduct, ListProduct, RemoveProduct, EditProduct
from web.routes import create_product_blueprint


def create_app():

    app = Flask(__name__,
                template_folder='web/templates',
                static_folder='web/static')
    
    repository = SQLiteProductRepository()

    uc_create = CreateProduct(repository)
    uc_list = ListProduct(repository)
    uc_delete_product = RemoveProduct(repository)
    uc_edit_product = EditProduct(repository)

    product_blueprint = create_product_blueprint(uc_create, uc_list, uc_delete_product, uc_edit_product)
    app.register_blueprint(product_blueprint)

    return app





if __name__ == "__main__":
    app = create_app()

    app.run(debug=True)