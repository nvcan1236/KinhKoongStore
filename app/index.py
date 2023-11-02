from flask import Flask, render_template, request
from app.data import products

app = Flask(__name__)
global products


@app.route('/')
def home():
    page = int(request.args.get('page')) if request.args.get('page') else 1
    pr = products[(page - 1) * 10:page * 10]
    return render_template('index.html', products=pr, page=page)


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
