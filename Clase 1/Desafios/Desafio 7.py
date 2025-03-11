#Desafio 7
# Escribir un programa que ingrese desde teclado una cadena de
# caracteres e imprima cuántas letras "a" contiene
palabra = input('Ingrese una cadena: ')

palabra = palabra.lower() # Escribe toda la palabra en minuscula

print(palabra.count('a')) # Cuenta la cantidad de veces que aparece un caracter