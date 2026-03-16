from fastapi import FastAPI, Depends
#from database import SessionLocal

# insertar los archivos de los metodos Get.
#from app_database.metodos.consultarApi import router
from metodos import consultarApi

app = FastAPI()
app.include_router(consultarApi.router, prefix="/productos")

{ 
# Incluir los varios routers
# app.include_router(users.router, prefix="/users", tags=["users"])
}

