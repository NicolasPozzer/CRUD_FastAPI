from fastapi import FastAPI
from models.product import Product #Importamos el Modelo para poder crear objetos de este modelo

app = FastAPI()

#Base de datos Logica
lista_productos = [
    {
        "id" : 1,
        "name": "Arroz",
        "price" : 120,
        "stock" : 10,
    },
    {
        "id" : 2,
        "name": "Chocolate",
        "price" : 200,
        "stock" : 10,
    }
]

#Endpoint que devuelve un mensaje
@app.get("/")
def message():
    return "Hello world"

#Endpoint que devuelve la lista de productos
@app.get("/productos")
def get_productos():
    return lista_productos

#Crear Productos
@app.post("/productos")
def create_product(product: Product):# Nos llega del cliente un obj de mi modelo
    lista_productos.append(product) #Lo metemos en la lista productos al producto
    return lista_productos # Y retornamos


@app.get("/productos/{id}")
def find_product(id: int):
    #Usamos filter que pide dos parametros y estos son "una funcion" y "la Lista"
    #En este caso usamos lambda para comparar si el id que entra por parametro,
    #es la misma que esta en el listado.
    #Usamos list al principio para convertirlo en una nueva lista y retornarlo.
    return list (filter(lambda item: item["id"] == id, lista_productos))


#End-Points con Parametros Query
# Ej. productos/?price=10&stock=20
@app.get("/productos/")
#La forma de declarar los parametros query es por medio de los parametros de la funcion
# ya que no son parametros de ruta de una url sino de un body de un obj. hay que declaralos
# de esta manera para que FastApi los detecte. Ej. stock: int como esta abajo...
def get_productos_by_stock(stock: int):
    return list(filter(lambda item: item["stock"] == stock, lista_productos))

#Editar
@app.put("/productos/{id}")
def edit_product(id: int, product: Product): #Necesitamos el id y el objeto con sus datos
    for index, item in enumerate(lista_productos): #Con esta linea tenemos acceso al item actual del producto y a su posicion.
        if item["id"] == id:
            lista_productos[index]["name"] = product.name  #Si el id de este item es igual al id que recibo como parametro
            lista_productos[index]["price"] = product.price #modifico los datos del producto actual.
            lista_productos[index]["stock"] = product.stock

    return lista_productos #Retornamos la lista actualizada


#Delete
@app.delete("/productos/{id}")
def delete_product(id: int):
    for item in lista_productos: #Usamos for comun ya que necesito acceder al valor del item no a la posicion.
        if item["id"] == id:
            lista_productos.remove(item)
    return lista_productos  #Una vez que borramos retornamos la nueva lista


