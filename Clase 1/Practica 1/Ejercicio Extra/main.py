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
