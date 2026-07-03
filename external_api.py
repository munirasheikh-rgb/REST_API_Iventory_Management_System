import requests
#retrieving a product using a barcode
def search_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (student project)"
    }

    response = requests.get(url , headers=headers)
    return response.json()
       
