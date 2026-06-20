from colorama import Fore, Back, init
init()

import productos
import validaciones

# MENU DE OPCIONES
pantalla = "Sistema de Gestión Básica de Productos"
print (Fore.RED + pantalla)

def menu():
    
    """ Muestra en pantalla las opciones del Sistema de Gestion:
    1. Ingresar productos
    2. Mostrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
    """
    print(Back.BLUE + Fore.WHITE + "1. Ingresar productos\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir\n" )

def separador() :
    # Un separador para aplicar a cada interracción con el menú
    print(Back.BLUE + Fore.WHITE +  "---" + Fore.RESET + Back.RESET)

def agregar_producto():
    """
    Solicita por consola un nombre de producto (str), categoría (str), un precio (float) y cant de stock (int).
    El bucle while se rompe:
     - al ingresar un id, nombre o categoría vacío
     - si la cantidad es invalida o menor o igual a 0
     - si precio es invalido menor o igual a 0
    Al tener todos los datos válidos se agrega al stock del modulo productos.
    """
    # [TO DO] la validación por id repetido.
    id_producto = ""
    nombre = ""
    categoria = ""
    cantidad = 0
    precio = 0.0
    productoAIngresar = {}

    while not validaciones.productoValido(id_producto, nombre, categoria, cantidad, precio):

        while validaciones.stringsNoVacio(id_producto, nombre, categoria):
            nombre = input("Ingrese nombre de producto: ").strip()
            categoria = input("Ingrese categoría de producto: ").strip()
            id_producto = input("Ingrese ID del producto: ").strip()
            if validaciones.repetido(id_producto.upper()):
                print("Lo siento, ese ID ya existe en nuestra base de datos")
                id_producto = ""

                
        idFormato = id_producto.upper()
        nombreFormateado = nombre.lower()
        categoriaFormateada = categoria.capitalize()
        
        
        while int(cantidad) <= 0:
            cantidad = input("Ingrese stock del producto (tiene que ser entero positivo):")
            if validaciones.stockInvalido(int(cantidad)):
                print("Lo siento el stock ingresado no es válido ")
                cantidad = 0

        precio = 0.0
        while float(precio) <= 0:
            precio = input("Ingrese un precio al producto (mayor a 0 y con dos decimales): ")
            if not isinstance(validaciones.conversion(precio), float):
                print("El precio ingresado no es válido")
                precio = 0.0
                

        productoAIngresar.update({"ID":idFormato})
        productoAIngresar.update({"nombre":nombreFormateado})
        productoAIngresar.update({"categoria":categoriaFormateada})
        productoAIngresar.update({"precio":float(precio)})
        productoAIngresar.update({"stock":int(cantidad)})
        #Agrego el diccionario como un item de la lista llamada stock.
        productos.stock.append(productoAIngresar)

        print(f"El Producto {productoAIngresar["nombre"]} fue agregado correctamente")

        separador()
        break
        
    separador()

def consultar_productos():
    """ Imprime en pantalla los productos y su ID.
    """
    if productos.stock:
        print(Back.GREEN + Fore.WHITE + "Lista de productos:" + Back.RESET + Fore.RESET)
        for i, producto in enumerate(productos.stock, start=1):
            print(Back.BLUE + Fore.WHITE + f"{i}. ID {producto["ID"]}: {producto["nombre"].capitalize()}")
            
    else:
        print(Back.RED + Fore.WHITE + "Lista de productos vacía." + Back.RESET + Fore.RESET)
    separador()    

def buscar_producto():
    """ Solicita el ID de un producto, si está en stock, imprime en pantalla el precio y la cantidad.
    Si no lo encuentra, dice que el producto no está disponible. Y ofrece la opcion de volver al menu inicial
    """

    while True:
        id_buscado = input("Ingrese ID de producto: ").strip().upper()
        for producto in productos.stock:
            if producto["ID"] == id_buscado:
                print(f"Aquí tenemos {producto.get("stock")} unidades de {producto.get("nombre")} a un precio de ${producto.get("precio")}")
                break 
        else:
            print(f"Lo siento no encontramos ningún producto con ID {id_buscado}")
        salir = input("Presione 's' para volver a Menu Inicial ")
        if salir.lower().strip() == "s":
            print("Volviendo a Menú Inicial...")
            break
    separador()

def borrar_producto():
    """Solicita el ID de un producto a borrar, si está en stock, lo borra del stock.
    Si no lo encuentra, dice que el producto no está disponible. Y ofrece la opcion de volver al menu inicial
    """
    while True:
        id_buscado = input("Ingrese ID de producto a eliminar del stock: ").strip().upper()
        for posicion, producto in enumerate(productos.stock):
            if producto["ID"] == id_buscado:
                productos.stock.pop(posicion)
                print(f"{producto.get("nombre").capitalize()} ha sido eliminado de la lista de productos")
                break 
        else:
            print(f"Lo siento no encontramos ningún producto con ID {id_buscado}")
        salir = input("Presione 's' para volver a Menu Inicial ")
        if salir.lower().strip() == "s":
            print("Volviendo a Menú Inicial...")
            break
    separador()


def mostrar_menu():
    while True:
        menu()
        opcion = input("Ingresa una opcion (1-5): ")

        match opcion.strip():
            case "1":
                agregar_producto()
            case "2":
                consultar_productos()
            case "3":
                buscar_producto()
            case "4":
                borrar_producto()
            case "5":
                print(Back.BLUE + Fore.WHITE + "Gracias, vuelvas pronto")
                print("Gestion de productos desarrollado por @GabrielKakazu")
                print("Talento Tech 2026 - Iniciación a Python")
                break
            case _:
                print(Back.BLUE + Fore.WHITE + "Lo siento, no ingresó una opción válida" + Fore.RESET + Back.RESET)

mostrar_menu()
        


