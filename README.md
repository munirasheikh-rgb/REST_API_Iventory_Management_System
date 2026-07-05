## Inventory Management system
A Flask-based REST API and Command Line Interface(CLI) application for managing inventory products.
The application allows users to create,view,update, and delete products while also supporting importing
product details from an external API using a product barcode.

# Features
- RESTful API built with Flask
- Command Line Interface(CLI) using argparse
- Create ne inventory products
- View all products
- Update exixting products
- Delete Products
- Import product details using barcode 
- Unit testing with pytest
- Mock API testing using unittest.mock
- Error handling for invalid requests and API connection

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
https://127.0.0.1.5555
```
