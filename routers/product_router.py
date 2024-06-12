from fastapi import APIRouter, Query, Path #Query y Path para validaciones.
from config.DataBase import lista_productos
from models.product import Product #Importamos el Modelo para poder crear objetos de este modelo
from fastapi import APIRouter, Query, Path
from typing import List, Optional

router = APIRouter()

# Endpoint que devuelve la lista de productos
#Response_model se usa para declarar el tipo de datos que se devolverá en la respuesta de un endpoint
@router.get("/productos", response_model=List[Product])#
def get_productos():
    return lista_productos

# Crear Productos
@router.post("/productos", response_model=Product)
def create_product(product: Product): # Nos llega del cliente un obj de mi modelo
    lista_productos.append(product) # Lo metemos en la lista productos al producto
    return product # y retornamos...

@router.get("/productos/{id}", response_model=Optional[Product])
def find_product(id: int = Path(gt=0)):
    #Usamos next ya que es mas eficiente porque encuentra y devuelve,
    # si no lo encuentra devuelve None y el mensaje
    producto = next((item for item in lista_productos if item.id == id), None)
    if producto:
        return producto
    return {"error": "Producto no encontrado"}

@router.put("/productos/{id}", response_model=Optional[Product])
def edit_product(id: int, product: Product): #Necesitamos el id y el objeto con sus datos.
    for index, item in enumerate(lista_productos): #Con esta linea tenemos acceso al item actual del producto y a su posicion.
        if item.id == id:
            lista_productos[index] = product #Busca el indice y lo mete al nuevo obj. editado.
            return product #Retornamos el obj. actualizado
    return {"error": "Producto no encontrado"}

@router.delete("/productos/{id}", response_model=Optional[dict])
def delete_product(id: int):
    for item in lista_productos: #Usamos for comun ya que necesito acceder al valor del item no a la posicion.
        if item.id == id: #Encontramos el item con el id que sea igual al id ingresado por el Usuario.
            lista_productos.remove(item) #Una vez que borramos retornamos un mensaje.
            return {"message": "Producto eliminado"}
    return {"error": "Producto no encontrado"}


#End-Points Externos de CRUD con Parametros Query
# Ej. productos/?price=10&stock=20
@router.get("/productos/stockigual", response_model=List[Product])
#La forma de declarar los parametros query es por medio de los parametros de la funcion
# ya que no son parametros de ruta de una url sino de un body de un obj. hay que declaralos
# de esta manera para que FastApi los detecte. Ej. stock: int como esta abajo...
def get_productos_by_stock(stock: int, price: float = Query(gt=0)):#Query para validar parametros tipo RequestParam
    return [item for item in lista_productos if item.stock == stock and item.price == price]