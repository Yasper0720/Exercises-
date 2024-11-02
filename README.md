Homecenter Database Management
Este proyecto utiliza SQLModel en Python para gestionar un sistema de inventarios en la cadena de tiendas Homecenter. 
El modelo de base de datos incluye tres tablas principales: Tienda, Producto, e Inventario. 
Estas tablas están relacionadas mediante una relación many-to-many, donde cada tienda puede tener múltiples productos y cada producto puede estar disponible en múltiples tiendas.


Características del Proyecto
CRUD Completo: Operaciones para crear, leer, actualizar y eliminar datos en las tablas de Tienda, Producto, y Inventario.
Relación Many-to-Many: Implementación de una relación de muchos a muchos entre Tienda y Producto a través de la tabla Inventario.
Persistencia: Base de datos SQLite para almacenamiento persistente.
Requisitos


Este proyecto requiere las siguientes bibliotecas de Python:

sqlmodel
sqlite3
