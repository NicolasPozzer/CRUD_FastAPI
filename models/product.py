from pydantic import BaseModel #Libreria necesaria para crear modelos del objeto
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None #En caso de que no se reciba un valor se le asigna None
    name: str
    price: float
    stock: int