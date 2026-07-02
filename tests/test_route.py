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
    
        