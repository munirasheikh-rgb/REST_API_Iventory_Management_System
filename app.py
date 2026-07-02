from flask import Flask,jsonify,request
from models import Product
app = Flask(__name__)

    
products = [
    Product(1,"Milk","Brookside","dairy",50),
    Product(2,"Bread","Festive","pastry",50)
]    

@app.route("/")
def index():
    return jsonify({"message":"Welcome to the inventory management website!"})

@app.route("/products",methods=["GET"])
def get_all_products():
    return jsonify([product.to_dict() for product in products])

@app.route("/products/<int:id>",methods=["GET"])
def get_product(id):
    product = next((p for p in products if p.id == id),None)
    if product:
        return jsonify(product.to_dict()),200
    else:
        return jsonify ({"error":"Product not Found"}),404
    
@app.route("/products", methods=["POST"])
def add_new_product():
    data = request.get_json()
    fields = ["name","brand","price","category"]
    for field in fields:
        if field not in data:
          return jsonify({"error":f"Enter a {field}"}),400
        
    new_id = max([p.id for p in products ]) +1 if products else 1
    new_product = Product(
        new_id,
        data["name"],
         data["brand"],
          data["category"],
           data["price"],
    )
    products.append(new_product)
    return jsonify(new_product.to_dict()),201







if __name__ == "__main__":
    app.run(port=5555,debug=True)