# Desafio 6
# Determinar si una palabra ingresada desde el teclado es un sustantivo
# propio o no
# Suponemos que un sustantivo propio siempre empieza por mayuscula
palabra = input('Ingrese una palabra: ')
if(palabra[0] >= 'A' and palabra[0]<= 'Z'):
    print('Es un sustantivo propio')
else:
    print('No es un sustantivo propio')