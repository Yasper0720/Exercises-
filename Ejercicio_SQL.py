from sqlmodel import Field, SQLModel, Session, create_engine, select, Relationship
from typing import List, Optional

class Tienda(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    ubicacion: str
    productos: List["Inventario"] = Relationship(back_populates="tienda")

class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    categoria: str
    precio: float
    tiendas: List["Inventario"] = Relationship(back_populates="producto")

class Inventario(SQLModel, table=True):
    tienda_id: Optional[int] = Field(default=None, foreign_key="tienda.id", primary_key=True)
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True)
    cantidad: int = Field(default=0)
    
    tienda: Optional[Tienda] = Relationship(back_populates="productos")
    producto: Optional[Producto] = Relationship(back_populates="tiendas")


engine = create_engine("sqlite:///homecenter.db")
SQLModel.metadata.create_all(engine)

# Crear una tienda
def crear_tienda(session: Session, nombre: str, ubicacion: str):
    tienda = Tienda(nombre=nombre, ubicacion=ubicacion)
    session.add(tienda)
    session.commit()
    session.refresh(tienda)
    return tienda

# Crear un producto
def crear_producto(session: Session, nombre: str, categoria: str, precio: float):
    producto = Producto(nombre=nombre, categoria=categoria, precio=precio)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

# Agregar un producto al inventario de una tienda (many-to-many)
def agregar_producto_inventario(session: Session, tienda_id: int, producto_id: int, cantidad: int):
    inventario = Inventario(tienda_id=tienda_id, producto_id=producto_id, cantidad=cantidad)
    session.add(inventario)
    session.commit()
    return inventario

# Leer productos en una tienda
def leer_productos_de_tienda(session: Session, tienda_id: int):
    consulta = select(Producto).join(Inventario).where(Inventario.tienda_id == tienda_id)
    return session.exec(consulta).all()

# Leer tiendas que tienen un producto específico
def leer_tiendas_con_producto(session: Session, producto_id: int):
    consulta = select(Tienda).join(Inventario).where(Inventario.producto_id == producto_id)
    return session.exec(consulta).all()

with Session(engine) as session:
    # Crear datos
    tienda = crear_tienda(session, nombre="Homecenter Medellín", ubicacion="Medellín")
    producto = crear_producto(session, nombre="Taladro", categoria="Herramientas", precio=150.00)

    # Agregar producto al inventario de la tienda
    inventario = agregar_producto_inventario(session, tienda_id=tienda.id, producto_id=producto.id, cantidad=50)

    # Leer productos en una tienda
    productos_tienda = leer_productos_de_tienda(session, tienda.id)
    print(f"Productos en {tienda.nombre}:", productos_tienda)

    # Leer tiendas que tienen un producto específico
    tiendas_con_producto = leer_tiendas_con_producto(session, producto.id)
    print(f"Tiendas con el producto {producto.nombre}:", tiendas_con_producto)
