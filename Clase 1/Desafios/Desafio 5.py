# Desafio 5
# Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que
# tenga más caracteres
cadena1 = input('Ingrese una palabra: ')
cadena2 = input('Ingrese otra palabra: ')
print('La palabra mas larga es: ', end='')
if(len(cadena1)>len(cadena2)):
    print(cadena1)
else:
    print(cadena2)
