from fastapi import FastAPI
from routers.product_router import router as procuct_rout #Con "as" cambio la variable del import
# me sirve para asignarle nombres a los routers y no dejarlo como router solo.

app = FastAPI() #Crea la Aplicacion

#Implementar Rutas o Controllers
app.include_router(procuct_rout)

#Endpoint que devuelve un mensaje
@app.get("/")
def message():
    return "Hello world"