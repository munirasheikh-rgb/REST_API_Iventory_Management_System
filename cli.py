import argparse
import requests
#url for the Flask API
URL =  "http://127.0.0.1:5555/products"
#retrive and display all products from inventory
def list_products():
    try:
        response = requests.get(URL)
        print(response.json())
    except requests.exceptions.RequestException:
       print("Could not connect to the API")

#create and send a new product to the API
def add_product(args):
    product = {
        "name":args.name,
        "brand":args.brand,
        "category":args.category,
        "price":args.price
    }
    try:
        response = requests.post(URL,json=product)
        print(response.json())
    except requests.exceptions.RequestException:
      print("Could not connect to the API")
    

#updating one or more fields of an existing product
def update_product(args):   
   updates= {}
   if args.name:
      updates["name"]=args.name 
   if args.brand:
      updates["brand"]=args.brand  
   if args.category:
      updates["category"]=args.category  
   if args.price:
      updates["price"]=args.price

   try:
    response =requests.patch(f"{URL}/{args.id}",json=updates)  
    print(response.json())
   except requests.exceptions.RequestException:
      print("Could not connect to the API")
  #delete a product by id 
def delete_product(args):
   
   try:
    response =requests.delete(f"{URL}/{args.id}")
    print(response.json())   
   except requests.exceptions.RequestException:
       print("Could not connect to the API")
      
parser = argparse.ArgumentParser(description="Inventory Management CLI")

subparsers =parser.add_subparsers(dest="command")
list_parser = subparsers.add_parser("list")#list all products command
#add product command and its required argument
add_parser = subparsers.add_parser("add",help= "Add a product")
add_parser.add_argument("--name",required=True,help="provide a name")
add_parser.add_argument("--brand",required=True,help="provide the brand of the product")
add_parser.add_argument("--category",required=True,help="add a category")
add_parser.add_argument("--price",required=True,type=int,help="add price of the item")

#update product command and its optional arguments
update_parser = subparsers.add_parser("update",help="Add a product to update or edit")
update_parser.add_argument("id",type=int)
update_parser.add_argument("--name")
update_parser.add_argument("--brand")
update_parser.add_argument("--category")
update_parser.add_argument("--price",type=int)
#delete product command
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id",type=int)

#command execution choosen by the user
if __name__ == "__main__":
 args = parser.parse_args()
 if args.command == "list":
    list_products()
 elif args.command == "add": 
    add_product(args)
 elif args.command == "update" :
    update_product(args)  
 elif args.command == "delete":
    delete_product(args)
 else:
    parser.print_help() 