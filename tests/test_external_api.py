from unittest.mock import patch
from external_api import search_product

@patch("external_api.requests.get")
def test_search_product_by_barcode(mock_get):
 mock_get.return_value.json.return_value = {
  "code":"0737628064502",
  "product":{
   "product_name":"Rice",
   "brands":"Dawat"
  }
 }
 data =search_product("0737628064502")
 assert data["code"] == "0737628064502"
 assert data["product"]["product_name"] =="Rice"