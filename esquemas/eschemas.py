from pydantic import BaseModel
from typing import Optional

# Esquema completo Taea (Modelo Pydantic)
class Producto(BaseModel):
    id_prod: Optional[int]  
    nom_prod: str
    proveedor: str

    class Config:
        orm_mode = True
