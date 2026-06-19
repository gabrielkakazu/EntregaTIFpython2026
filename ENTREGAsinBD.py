import datetime as fecha
import productos
import validaciones

# MENU DE OPCIONES
pantalla = "Sistema de Gestión Básica de Productos"
print (pantalla)

def menu():
    # TODO agregar colorama al menú
    """ Muestra en pantalla las opciones del Sistema de Gestion:
    1. Ingresar productos
    2. Mostrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
    """
    print(" 1. Ingresar productos\n 2. Mostrar productos\n 3. Buscar producto\n 4. Eliminar producto\n 5. Salir\n")

def separador() :
    # Un separador para aplicar a cada interracción con el mení
    print("---")

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
            id_producto = input("Ingrese ID del producto: ").strip()
            nombre = input("Ingrese nombre de producto: ").strip()
            categoria = input("Ingrese categoría de producto: ").strip()
            
        # if validaciones.repetido(id):
        #     print("Lo siento, ese ID ya existe en nuestra base de datos")
        #     break
        
        idFormato = id_producto.upper()
        nombreFormateado = nombre.lower()
        categoriaFormateada = categoria.capitalize()
        fechaDeImportación = fecha.date.today()
        
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
    # [TO DO] forma de presentación de la lista de productos. Agregar colorama.
    """ Imprime en pantalla los productos agregados y su precio.
    """
    if productos.stock:
        print("Lista de productos:")
        for i, producto in enumerate(productos.stock, start=1):
            print(f"{i}. {producto}")
            
    else:
        print("Lista de productos vacía.")
    separador()    

def buscar_producto():
    """ Solicita el nombre de un producto, si está en la colección, imprime en pantalla el precio del producto.
    Si no lo encuentra, dice que el producto no está disponible
    """

    """
    while True:
        productoBuscado = input("Ingrese nombre de producto: ").strip().lower()
        if productoBuscado not in productos:
            print("Lo siento, el producto no esta disponible... ")
                    
        else:
            print(f"Aquí tenemos {productoBuscado} a un precio de ${productos.get(productoBuscado)}")
                
            salir = input("Presione 's' para volver a Menu Inicial ")
            if salir.lower().strip() == "s":
                print("Volviendo a Menú Inicial...")
                break
    """

def borrar_producto():
    """
    while True:
        productoABorrar = input("Ingrese nombre de producto a eliminar: ")
        if productoABorrar.lower().strip() not in productos:
            print("Lo siento, el producto no existe en nuestra BD")
            break
        else:
            print(f"Eliminamos {productoABorrar} de nuestra BD")
            del productos[productoABorrar]
            break
    separador()
    """

            

    """if productos:
        productoABorrar = input("Ingrese nombre de producto a borrar: ")
        if productoABorrar in productos:
            productos.pop(productoABorrar)
            print(f"Se eliminó {productoABorrar} de la lista.")
            separador()
        else:
            print(f"No se encuentra en la lista {productoABorrar}")
            separador()"""

def mostrar_menu():
    # AGREGAR COLORAMA a la despedida
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
                print("Gracias, vuelvas pronto")
                print("Gestion de productos desarrollado por @GabrielKakazu")
                print("Talento Tech 2026 - Iniciación a Python")
                break
            case _:
                print("Lo siento, no ingresó una opción válida")

mostrar_menu()
        


