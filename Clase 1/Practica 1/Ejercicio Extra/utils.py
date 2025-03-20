def agregarProducto(inventario = dict):
    inventario.update({input('Ingrese el nombre del producto: '): input('Ingrese la cantidad de ese producto: ')})
    print('Elemento agregado correctamente!')
    print('')
