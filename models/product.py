from pydantic import BaseModel, Field #Libreria necesaria para crear modelos del objeto. Field para validaciones!
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = 999 #En caso de que no se reciba un valor se le asigna 999
    name: str = Field(default='New Product', min_length=5, max_length=15)#Validaciones que agregan un valor por defecto
                                                                         # con un minimo de 5 y maximo de 10 caracteres
    price: float = Field(default=0, ge=0, le=1000) #Mayor o igual a 0 y menor a 1000
    stock: int = Field(default=0, gt=0)