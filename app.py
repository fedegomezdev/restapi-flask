from flask import Flask, jsonify, request #jsonify nos permite pasar de un objeto a un json por ejemplo y request proporciona los datos que nos envian
from product import products

app = Flask(__name__) #app es el servidor en si

@app.route('/ping')
def ping():
    return jsonify({'message':'pongo!'})


@app.route('/products')
def getProduct():
    return jsonify({'products':products, 'message':'lista de productos'})    


@app.route('/products/<string:product_name>')
def getOneProduct(product_name):
    productFound = [product for product in products if product_name == product['name']]
    if len(productFound) > 0 :
        return jsonify({'product': productFound[0]})
    return jsonify({'message':'no se encontraron productos'})


@app.route('/products', methods=['POST'])
def postProduct():
    newProduct = {
        'name': request.json['name'],
        'price': request.json['price'],
        'cantidad': request.json['cantidad']
    }
    products.append(newProduct)
    return jsonify({'message': 'producto agregado', 'product': products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def putProduct(product_name):
    updateProduct=[ product for product in products if product['name'] == product_name ]    
    if len(updateProduct) > 0:
        updateProduct[0]['name'] = request.json['name']
        updateProduct[0]['price'] = request.json['price']
        updateProduct[0]['cantidad'] = request.json['cantidad']
        return jsonify({'message': 'producto  modificado', 'products': products})
    return jsonify({'message':'producto no encontrado'})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    delProduct = [ product for product in products if product['name'] == product_name ]
    if len(delProduct) > 0:
        products.remove(delProduct[0]) #le paso el primer objeto de la lista
        return jsonify({'message': 'producto eliminado', 'productos': products})
    return jsonify({'message':'producto no encontrado'})


if __name__ == '__main__': #si es la aplicacion principal
    app.run(debug = True, port=4000) #para que se reinicie cuando hacemos cambios