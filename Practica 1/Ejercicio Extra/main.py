""" Creación de un programa básico de gestión de inventario.
Desarrollar un programa en Python que permita gestionar un inventario
simple de productos, incluyendo funciones básicas como agregar productos,
eliminar productos y mostrar el inventario.
El programa debe tener un menú interactivo que permita al usuario
seleccionar las siguientes operaciones:
Agregar un nuevo producto al inventario, solicitando al usuario el nombre y
la cantidad inicial del producto.
Eliminar un producto existente del inventario, solicitando al usuario el
nombre del producto a eliminar.
Mostrar el inventario actual, que incluya el nombre y la cantidad de cada
producto.
Salir del programa.
El inventario puede ser almacenado utilizando un diccionario simple, donde
las claves sean los nombres de los productos y los valores sean las cantidades. Se
deben manejar situaciones simples como la introducción de productos duplicados
o la eliminación de productos inexistentes. """
import utils
opcion = 0
inventario = {}
while opcion != 4:
    print('Bienvenido al menu del inventario! ')
    print('Que accion deseas realizar? ')
    print('1. Agregar un Producto')
    print('2. Eliminar un producto ')
    print('3. Mostrar el inventario')
    print('4. Cerrar')
    print('')
    opcion = input('Ingrese la opcion: ')
    print('')
    if opcion.isdigit() == True:
        opcion = int(opcion)
    else:
        print('Ingresa un digito!!')
        continue
    match opcion:
        case 1:
            utils.agregarProducto(inventario)
        case 2:
             utils.eliminarProducto(inventario)
        case 3:
            utils.mostrarInventario(inventario)
        case 4:
            print('Cerrando programa, gracias por utilizarlo!!...')
        case _:
            print('Opcion invalida, ingresa una opcion correcta! ')
