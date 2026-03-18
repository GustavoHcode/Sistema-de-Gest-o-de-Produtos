from flask import Blueprint, render_template, request, redirect, url_for 

def create_product_blueprint(uc_create, uc_list, uc_delete_produto):
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


    return bp

    
    
    