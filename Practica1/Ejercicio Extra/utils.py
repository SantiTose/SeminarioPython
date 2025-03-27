def agregarProducto(inventario = dict):
    inventario.update({input('Ingrese el nombre del producto: '): input('Ingrese la cantidad de ese producto: ')})
    print('Elemento agregado correctamente!')
    print('')

def eliminarProducto(inventario = dict):
    nom = input('Ingrese el nombre del producto: ')
    if nom in inventario.keys():
        inventario.pop(nom)
        print('Elemento borrado correctamente!!')
    else:
        print('No existe esa clave. Ingresa una clave valida! ')
    print('')

def mostrarInventario(inventario = dict):
    for elem in inventario:
        val = inventario[elem]
        print(f'Producto: "{elem}" Cantidad: "{val}"' )
    print('')
