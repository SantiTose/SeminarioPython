# Desafio 3
# Dado una letra ingresada por el teclado, queremos saber si es mayúscula
# o minúscula
letra = input('Ingrese una letra: ')
if(letra >='a' and letra <='z'):
    print('Es minuscula')
elif letra >='A' and letra <='Z':  
    print('Es mayuscula')
else:
    print('No es una letra')