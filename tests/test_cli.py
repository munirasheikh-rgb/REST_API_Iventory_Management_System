from cli import list_products,add_product
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