from decimal import Decimal
from pydantic import BaseModel, Field


class ServicioSchema(BaseModel):
    nombre: str
    descripcion: str
    precio: Decimal = Field(gt=0)
    activo: bool = True


class Servicio:
    def __init__(self, nombre: str, descripcion: str, precio: Decimal, id_servicio: int | None = None,
                 activo: bool = True):
        self.id_servicio = id_servicio
        
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.activo = activo

    def __str__(self):
        return f"Servicio(id={self.id_servicio}, nombre='{self.nombre}', precio={self.precio})"
