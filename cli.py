import argparse
import requests

URL =  "http://127.0.0.1:5555/products"

def list_products():
    response = requests.get(URL)
    print(response.json())

def add_product(args):
    product = {
        "name":args.name,
        "brand":args.brand,
        "category":args.category,
        "price":args.price
    }

    response = requests.post(URL,json=product)
    print(response.json())

parser = argparse.ArgumentParser(description="Inventory Management CLI")

subparsers =parser.add_subparsers(dest="command")
list_parser = subparsers.add_parser("list")

add_parser = subparsers.add_parser("add",help= "Add a product")
add_parser.add_argument("--name",required=True,help="provide a name")
add_parser.add_argument("--brand",required=True,help="provide the brand of the product")
add_parser.add_argument("--category",required=True,help="add a category")
add_parser.add_argument("--price",required=True,type=int,help="add price of the item")




if __name__ == "__main__":
 args = parser.parse_args()
 if args.command == "list":
    list_products()
 if args.command == "add": 
    add_product(args)