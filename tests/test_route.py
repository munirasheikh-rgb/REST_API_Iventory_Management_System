from app import app,products
def test_home_route():
    """displays a welcome message"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to the inventory management website!"

def test_get_all_products():
    """retrieve all product details""" 
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.get_json(),list) 

def tests_a_single_product():
    """gets a single product fro the list""" 
    client = app.test_client()
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Milk"

def test_product_not_found():
    """returns an error when there is no product with the id """
    client = app.test_client()
    response = client.get("/products/90")
    assert response.status_code == 404

def tests_add_new_product():
    """adds new product to the list"""
    client = app.test_client()  
    initial_count = len(products)
    new_product = {
        "name":"Rice",
        "brand":"Dawati",
        "category":"grains",
        "price": 450
    }  
    response = client.post("/products",json=new_product)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] =="Rice"
    assert data["brand"] =="Dawati"
    assert data["category"] =="grains"
    assert data["price"] == 450
    assert "id" in data
    assert len(products) == initial_count + 1
    
def tests_update_product():
    """Updates the existing product"""
    client = app.test_client() 
    update_data ={"price":600}
    response = client.patch("/products/1",json=update_data) 
    assert response.status_code == 200
    data =response.get_json()
    assert data["id"]==1
    assert data["price"] == 600

def tests_delete_product():
    """deletes a product by id"""
    client = app.test_client() 
    response = client.delete("/products/2")
    assert response.status_code == 200
    data =response.get_json()
    assert data["message"] == "Product deleted successfully!"

def test_external_product_route():
    """fetch product details from an external API by querrying barcode"""
    client = app.test_client() 
    response = client.get("/external-product?barcode=737628064502")
    data = response.get_json()
    assert response.status_code ==200
    assert "barcode" in data
    assert "brand" in data
    assert "category" in data
    assert "name" in data
def test_import_external_product():
   """adds an external product from the API to the products list"""
   client = app.test_client() 
   initial_count = len(products)

   response =client.post("/products/import?barcode=737628064502")
   assert response.status_code == 201
   data = response.get_json()
   assert"id" in data
   assert"name" in data
   assert"brand" in data
   assert"category" in data
   assert"price" in data

  
   

   