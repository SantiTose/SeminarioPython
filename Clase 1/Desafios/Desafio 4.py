# Desafio 4
# Dado un caracter ingresado por el teclado, queremos saber si es una
#comilla o no
simbolo = input('Ingrese un simbolo: ')
if simbolo == '\'' or simbolo == '\"':
    print('Es una comilla')
else:
    print('No es una comilla')