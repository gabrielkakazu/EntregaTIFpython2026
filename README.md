# EntregaFinalPython2026TalentoTech
CRUD de productos del curso Iniciación a la Programación con Python (TalentoTech2026)

## Funcionalidades de la aplicación
La aplicación permite:
* Registrar nuevos productos.
* Visualizar datos de los productos registrados.
* Actualizar datos de productos, mediante su ID.
* Eliminación de productos, mediante su ID.
* Búsqueda de productos, mediante su ID.
* Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario

## Menu de entrada
Muestra en pantalla las opciones del Sistema de Gestion:
    1. Ingresar productos
    2. Mostrar productos
    3. Buscar producto
    4. Eliminar producto
    5. Actualizar producto
    6. Alerta Stock Bajo
    7. Salir

## Modularizacion
+ Se incorpora el modulo colorama para un tratamiento visual.
+ Las funciones de validacion están en el modulo validaciones:
    - que los inputs del usuario no sean vacios
    - que los precios y la cantidad de stock no sean negativos
    - que el ID al ingresar un producto no este repetido.
+ La lista de stock está en el modulo productos

## Funciones
Las herramientas del CRUD estan estructuradas en diferentes funciones para ordenar el codigo:
    - menu()
    - agregar_producto()
    - consultar_producto()
    - buscar_producto()
    - borrar_producto()
    - actualizar_producto()
    - alerta_stock_bajo()
    - mostrar_menu() que es la funcion principal.



Autor: Kakazu, Gabriel Nicolás
2026
