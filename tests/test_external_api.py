from external_api import search_product

def search_product_by_barcode():
 data = search_product("737628064502")
 assert isinstance(data,dict)
 assert data["code"] == "737628064502"
 