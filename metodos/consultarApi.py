from fastapi import APIRouter, Query, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from modelos import model_producto
from app_database.esquemas import eschemas

router = APIRouter()
@router.get("/")
async def consultar():
    return "Consultar Alumnos del Programa...."

@router.get("/prod_all")
def get_users(db: Session = Depends(get_db)):
    # Ejemplo: obtener todos los usuarios
    producto = db.query(model_producto.Producto).all()
    return producto

@router.get("/prod/{prodId}")
def get_id(prodId : int, db: Session = Depends(get_db)):
    # Ejemplo: obtener un solo usuario
    producto = db.query(model_producto.Producto).filter(model_producto.Producto.id_prod == prodId).first()
    if (producto):
        # f"Producto: {producto.nom_prod}"
        return producto
    return "Producto no existe.... "

@router.get("/produc/{prodId}")
def get_id(prodId : int, db: Session = Depends(get_db)):
    # Ejemplo: obtener un solo usuario
    producto = db.query(model_producto.Producto).get(prodId)
    if (producto):
        return producto
    else:
         raise HTTPException(status_code=404, detail=f"Tarea con id {prodId} no encontrada")
    

## Ingresar un producto
@router.post("/add", response_model=eschemas.Producto, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: eschemas.Producto, sesion: Session = Depends(get_db)):
    productoAdd = model_producto.Producto(
        id_prod= producto.id_prod,
        nom_prod= producto.nom_prod,
        proveedor= producto.proveedor,
        )

    sesion.add(productoAdd)
    sesion.commit()
    sesion.refresh(productoAdd)

    return productoAdd

## actualizar un producto
@router.put("/update/{id_prod}", response_model=eschemas.Producto)
def update_user(id_prod: int, producs: eschemas.Producto, db: Session = Depends(get_db)):
    producto = db.query(model_producto.Producto).filter(model_producto.Producto.id_prod == id_prod).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")   
    # Actualizar campos
    producto.id_prod = producs.id_prod
    producto.nom_prod = producs.nom_prod
    producto.proveedor = producs.proveedor
    db.commit()
    db.refresh(producto)
    
    return producto

## borrar un campo de la tabla
@router.delete("/borrar/{id_prod}")
def borrar_Producto(id_prod: int, db: Session = Depends(get_db)):
    # Buscar el ítem en la base de datos
    producto = db.query(model_producto.Producto).filter(model_producto.Producto.id_prod == id_prod).first()   
    # Si no se encuentra, lanzar error 404
    if producto is None:
        raise HTTPException(status_code=404, detail="Product not found")  
    # Eliminar el prducto
    db.delete(producto)
    db.commit()   
    # Respuesta de éxito
    return {"detail": "producto eliminado...."}
