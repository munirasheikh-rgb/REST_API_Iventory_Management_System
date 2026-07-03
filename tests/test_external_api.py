from external_api import search_product

def test_search_product_by_barcode():
 data = search_product("0737628064502")
 assert isinstance(data,dict)
 assert data["code"] == "0737628064502"
 assert "product" in data