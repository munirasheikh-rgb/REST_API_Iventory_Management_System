from unittest.mock import patch
from cli import list_products,add_product,update_product,delete_product

URL =  "http://127.0.0.1:5555/products"

class AddArgs:
    name ="Rice"
    brand = "Dawat"
    category ="grains"
    price = 450
#mock GET request so no real API call is made  
@patch("cli.requests.get")
def test_list_product(mock_get,capsys):
        """simulate JSON response return by the API"""
        mock_get.return_value.json.return_value =[
            {"id":1,
            "name":"Milk",
            "brand":"Brookside",
            "category":"dairy",
            "price":75}
    ]    
        list_products()
        captured = capsys.readouterr()
        assert "Milk" in captured.out 
        mock_get.assert_called_once_with(f"{URL}")#assert get request was made once
#mock post request to avoid creating a real product
@patch("cli.requests.post")
def test_add_product(mock_post,capsys):
        """simulate JSON response returned by the API"""
        mock_post.return_value.json.return_value = {
              "id":3,
            "name":"Rice",
            "brand":"Dawat",
            "category":"grains",
            "price":450 
        }
        add_product (AddArgs) 
        captured =capsys.readouterr() 
        assert "Rice"in captured.out
        assert "grains" in captured.out
        assert "Dawat" in captured.out
        mock_post.assert_called_once_with(URL,json={
               "name":"Rice",
               "brand":"Dawat",
               "category":"grains",
               "price":450
        })

class UpdatePriceArgs:
       id =1
       name = None
       brand = None
       category = None
       price= 75

 #mock patch request to simulate updating a product
@patch("cli.requests.patch")       
def test_update_product_price(mock_patch,capsys):
       mock_patch.return_value.json.return_value ={
           "id":1,
            "name":"Milk",
            "brand":"Brookside",
            "category":"dairy",
            "price":75   
       }
       update_product(UpdatePriceArgs)
       captured = capsys.readouterr()
       assert "75" in captured.out
       mock_patch.assert_called_once_with(f"{URL}/1",json={"price":75})

class UpdateNameArgs:
       id=1
       name = "Cheese"
       brand = None
       category = None  
       price = None

@patch("cli.requests.patch")
def test_update_product_name(mock_patch,capsys):
       mock_patch.return_value.json.return_value = {
              "id":1,
            "name":"Cheese",
            "brand":"Brookside",
            "category":"dairy",
            "price":75   
       }   
       update_product(UpdateNameArgs)
       captured = capsys.readouterr()
       assert "Cheese" in captured.out       
       mock_patch.assert_called_once_with(f"{URL}/1",json={"name":"Cheese"})


class DeleteArgs:
       id = 3 
#mock delete quest to simulate deleting na product
@patch("cli.requests.delete")      
def test_delete_product(mock_delete,capsys):
      mock_delete.return_value.json.return_value ={
             "message":"Product deleted successfully!"
      }

      delete_product(DeleteArgs)
      captured = capsys.readouterr()
      assert "Product deleted successfully!" in captured.out
      mock_delete.assert_called_once_with(f"{URL}/3")
