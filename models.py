class Product:
    def __init__(self,id,name,brand,category,price):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price

    def to_dict(self):
        return ({
            "id":self.id ,
            "name":self.name,
            "brand":self.brand,
            "price":self.price,
            "category":self.category
})