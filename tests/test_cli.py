from cli import list_products,add_product,update_product,delete_product
class Args:
    name ="Rice"
    brand = "Dawat"
    category ="grains"
    price = 450

def test_list_product(capsys):
        list_products()
        captured = capsys.readouterr()
        assert "Milk" in captured.out or "Bread" in captured.out
def test_add_product(capsys):
        add_product (Args) 
        captured =capsys.readouterr() 
        assert "Rice"in captured.out
        assert "grains" in captured.out
        assert "Dawat" in captured.out

class UpdatePriceArgs:
       id =1
       name = None
       brand = None
       category = None
       price= 75
def test_update_product_price(capsys):
       update_product(UpdatePriceArgs)
       captured = capsys.readouterr()
       assert "75" in captured.out


class UpdateBrandArgs:
       id =1
       name = None
       brand = "Brookside"
       category = None
       price= None
def test_update_product_brand(capsys):
       update_product(UpdateBrandArgs)
       captured = capsys.readouterr()
       assert "Brookside" in captured.out

               
class UpdateCategoryArgs:
       id =1
       name = None
       brand = None
       category = "dairy"
       price= None
def test_update_product_category(capsys):
       update_product(UpdateCategoryArgs)
       captured = capsys.readouterr()
       assert "dairy" in captured.out

class UpdateAllArgs:
       id =1
       name = "Milk"
       brand ="Brookside"
       category = "dairy"
       price= 75
def test_update_products(capsys):
       update_product(UpdateAllArgs)
       captured = capsys.readouterr()
       assert "Milk" in captured.out
       assert "Brookside" in captured.out
       assert "dairy" in captured.out
       assert "75" in captured.out

class DeleteArgs:
       id = 3       
def test_delete_product(capsys):
      delete_product(DeleteArgs)
      captured = capsys.readouterr()
      assert "Product deleted successfully!" in captured.out
