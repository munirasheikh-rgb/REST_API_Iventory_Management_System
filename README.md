## Inventory Management system
A Flask-based REST API and Command Line Interface(CLI) application for managing inventory products.
The application allows users to create,view,update, and delete products while also supporting importing
product details from an external API using a product barcode.

# Features
- RESTful API built with Flask
- Command Line Interface(CLI) using argparse
- Create new inventory products
- View all products
- Update existing products
- Delete Products
- Import product details using barcode 
- Unit testing with pytest
- Mock API testing using unittest.mock
- Error handling for invalid requests and API connection Failure

## Technologies Used
- Python
- Flask
- Requests
- argparse 
- pytest
- unittest.mock
- OpenFoodFacts API
- Git & Github

## Project Structure
 ```
 inventory-management-system/
│
├── app.py
├── cli.py
├── external_api.py
├── models.py
├── requirements.txt
│
├── tests/
│   ├── test_route.py
│   ├── test_cli.py
│   └── test_external_api.py
│
└── README.md
```
## Installation
- Clone the repository
```bash
git clone https://github.com/munirasheikh-rgb/REST_API_Iventory_Management_System.git
 ```
- Navigate into the Project
```bash
cd REST_API_Inventory_Management_System 
```
- Create and activate the virtual environment using pipenv
```bash
pipenv shell
```
- Install Dependencies
```bash
pip install -r requirement.txt
```
## Running The Flask API
```bash
python app.py
```
- The API runs on 
```
http://127.0.0.1.5555
```
## CLI Commands

### View Products
```
python cli.py list
```
### Add Product
```
python cli.py add --name Rice --brand Dawat --category grains --price 450
```
### Update Product
```
 python cli.py update 1 --price 600
```
### Delete Product
```
python cli.py delete 1
```

## API Endpoint Details
```bash
Method | Endpoint   | Description
-------------------------------------
GET|   /products |  Retrieve all Products |
POST|   /products |  Create a new Product |
PATCH|   /products\<id> |  Update a product |  
DELETE|   /products\<id> |  Delete product |
POST|    /products/import?barcode= | Imports a product using barcode | 

```  
## Testing 
- Run all tests
```
pytest
```
- Run API test
```
pytest tests/test_route.py
```
- Run CLI Tests
```
pytest tests/test_cli.py
```
- Run External API test
```
pytest tests/test_external_api.py
```

## Error Handling 
The application handles:
- Missing required Fields
- Invalid Product IDs
- API connection Failure
- Missing barcode
- External API Failure

## Future Improvements
- Database intergration (MySQL)
- User Authentication 
- Product filtering
- Inventory stock Management

### What I learnt
During this project i have learnt to:
- Build RESTful APIs using Flask.
- Create command line interface using argparse .
- Intergrating external APIs into Flask python application.
- Write unit test using pytest and unittest.mock to simulate API response 
- Isolate external dependencies during testing

# Author 
Munira Hassan