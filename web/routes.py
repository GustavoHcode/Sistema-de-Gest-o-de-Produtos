from flask import Blueprint, render_template, request, redirect, url_for 
from core.domain.product.product import Product
def create_product_blueprint(uc_create, uc_list, uc_delete_produto, uc_edit_product):
    bp = Blueprint('products', __name__)

    @bp.route('/')
    def home_page():
        return render_template('index.html')
    
    @bp.route('/produtos')
    def produto_page():
        
        produtos = uc_list.execute()
    
        return render_template('products.html', produtos=produtos)
    
    @bp.route('/produtos/novo', methods=['POST'])
    def cadastrar_produtos():
        dados = {
            'name': request.form.get('nome'),
            'amount': int(request.form.get('quantidade')),
            'sale_price': float(request.form.get('preco_venda')),
            'sale_buy': float(request.form.get('preco_compra'))

        }
        uc_create.execute(dados)

        return redirect(url_for('products.produto_page'))
    
    @bp.route('/produtos/deletar/<int:id>', methods=['GET'])
    def deletar_produto(id):
    
        uc_delete_produto.execute(id)

        return redirect(url_for('products.produto_page'))

    @bp.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
    def editar_produto(id):
        if request.method == 'POST':
            product = Product(
                id=id, 
                name=request.form.get('nome'),
                amount=int(request.form.get('quantidade', 0)),
                sale_price=float(request.form.get('preco_venda', 0)),
                buy_price=float(request.form.get('preco_compra', 0))
            )
         
            uc_edit_product.execute(product)
            return redirect(url_for('products.produto_page'))

    
        todos_produtos = uc_list.execute()
        produto = next((p for p in todos_produtos if p['id'] == id), None)
        if not produto:
            return "Produto não encontrado", 404

        return render_template('edit-produto.html', produto=produto)
    @bp.route('/metricas')
    def page_financeiro():
        return render_template('metricas.html')

    @bp.route('/vendas')
    def vendas_page():
        return render_template('vendas.html')
    
    return bp

    
    
    