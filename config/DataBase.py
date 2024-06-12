# Base de datos lógica como una lista de instancias de Product
from models.product import Product

lista_productos = [
    Product(id=1, name="Arroz", price=120.0, stock=10),
    Product(id=2, name="Chocolate", price=200.0, stock=10),
]
