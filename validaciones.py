import productos

def productoValido(id, nombre, categoria, cantidad, precio):
    return stringsNoVacio(id, 
                          nombre, 
                          categoria) and not stockInvalido(
                              cantidad) and conversion(precio)>0

def stringsNoVacio(st1, st2, st3):
    return not st1 or not st2 or not st3

def conversion(precio) :
    try:
        # Solicitamos el ingreso de un dato (siempre se recibe como str)
        # precio = input("Ingresá un precio con decimales (usá punto para los decimales): ")
        
        # Intentamos realizar la conversión a float
        conversion = float(precio)
        
        # Si la conversión es exitosa, mostramos el resultado
        return conversion

    except ValueError:
        # Este bloque se ejecuta si la conversión falla (ej: si el usuario ingresó 'abc')
        print("[ERROR] Debés ingresar un valor numérico válido. No se admiten letras ni símbolos.")

def stockInvalido(stock):
    return not isinstance(stock, int) or stock <= 0

def repetido(id):
    for producto in productos.stock:
        if producto["ID"] == id:
            return True
    
    return False
