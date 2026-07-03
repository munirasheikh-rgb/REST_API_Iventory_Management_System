from flask import Flask,jsonify,request
from external_api import search_product
from models import Product
app = Flask(__name__)

 #in-memory product data   
products = [
    Product(1,"Milk","Brookside","dairy",50),
    Product(2,"Bread","Festive","pastry",50)
]    
#home route displays welcome message
@app.route("/")
def index():
    return jsonify({"message":"Welcome to the inventory management website!"})
# route about the app with afew details
@app.route("/about")
def about():
    return jsonify({"application":"Inventory Management System",
                    "framework":"Flask",
                    "description":"A REST API for managing inventory items with CRUD operations and external API intergration"
                    })

#retrieving  all products and converting them to a dictionary
@app.route("/products",methods=["GET"])
def get_all_products():
    return jsonify([product.to_dict() for product in products])

#get a single product by id
@app.route("/products/<int:id>",methods=["GET"])
def get_product(id):
    product = next((p for p in products if p.id == id),None)
    if product:
        return jsonify(product.to_dict()),200
    else:
        return jsonify ({"error":"Product not Found"}),404 #returning an error(404) if no product matches the id
    
  #adding new product and appending it to the existing product list  
@app.route("/products", methods=["POST"])
def add_new_product():
    data = request.get_json()
    fields = ["name","brand","price","category"]#required fields for creating a product
    for field in fields:
        if field not in data:
          return jsonify({"error":f"Enter a {field}"}),400 #returning an error if the field is undefined
        
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

#updating an existing product
@app.route("/products/<int:id>",methods=["PATCH"])
def update_product(id):
   data = request.get_json()
   product = next((p for p in products if p.id == id),None)
   if not product:
       return jsonify({"error":"Product not found"}),404
   fields = ["name","brand","price","category"]#fields open for update
   for field in fields:
       if field in data:
           setattr(product,field,data[field])# updating only the fields provided dynamically
   return jsonify(product.to_dict()),200
  
#remove a product from the system
@app.route("/products/<int:id>",methods=["DELETE"])
def remove_product(id):
    global products
    product = next((p for p in products if p.id == id),None)
    if not product:
        return jsonify({"error":"Product not found"}),404
    products = [p for p in products if p.id != id]
    return jsonify ({"message":"Product deleted successfully!"}),200

@app.route("/external-product")
def external_product():
    barcode =request.args.get("barcode")
    data = search_product(barcode)
    product = data.get("product",{})
    
    return jsonify(
        {
            "barcode":data.get("code"),
            "name":product.get("Product_name") or "unknown product",
            "brand":product.get("brands"),
            "category":product.get("categories"),

        }
    )
@app.route("/products/import",methods=["POST"])
def import_external_product():
    barcode=request.args.get("barcode")
    if not barcode:
        return jsonify({"error":"Barcode is required"}),400
    data =search_product(barcode)
    product_data = data.get("product",{})
    new_id =max([p.id for p in products]) +1 if products else 1
    new_product =Product(
        new_id,
        product_data.get("product_name") or "unknown product",
        product_data.get("brands") or "unknown brand",
        product_data.get ("categories") or "unknown category",
        0
    )
    products.append(new_product)
    return jsonify(new_product.to_dict()),201



if __name__ == "__main__":
    app.run(port=5555,debug=True)