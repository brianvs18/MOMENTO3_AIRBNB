from flask import Flask, jsonify, request

app = Flask(
    __name__)  ## me devuelve un objeto app y este es l aplicacion de servido o el servidor se necesita inicializar

from products import products


@app.route('/ping')
def ping():
    return jsonify({"message": "pong!!"})


@app.route('/products')
def getProperties():
    return jsonify({'products': products, 'mesagge': 'products list'})


@app.route('/products/<int:product_id>')
def getProperty(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({"mesagge": "product not found", "statusCode": 500})


@app.route('/products', methods=['POST'])
def addProperty():
    new_product = {
        "adress": request.json['adress'],
        "area": request.json['area'],
        "id": request.json['id'],
        "name": request.json['name'],
        "price": request.json['price'],
        "rooms": request.json['rooms']
    }
    products.append(new_product)
    return jsonify({"mesagge": "the product has been saved", "products": products})


@app.route('/products/<int:product_id>', methods=['PUT'])
def editProperty(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['adress'] = request.json['adress']
        productsFound[0]['area'] = request.json['area']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['rooms'] = request.json['rooms']

        return jsonify({
            "mesagge": "product update",
            "product": productsFound[0]
        })
    return jsonify({
        "mesagge": "product not found",
    })


@app.route('/products/<int:product_id>', methods=['DELETE'])
def deleteProperty(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "mesagge": "product deleted",
            "product": products
        })
    return jsonify({
        "mesagge": "product not found",
    })


if __name__ == "__main__":
    app.run(debug=True, port=4000)
