from flask import Flask, render_template, request
from app.data import products

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', products=products)


@app.route('/product')
def product():
    id_product = int(request.args.get('id'))
    p = products[id_product]
    return render_template('product.html', product=p)


@app.route('/payment')
def payment():
    id_product = int(request.args.get('id'))
    q = int(request.args.get('amount'))
    p = products[id_product]
    return render_template('payment.html', product=p, amount=q)


if __name__ == '__main__':
    app.run(debug=True)
