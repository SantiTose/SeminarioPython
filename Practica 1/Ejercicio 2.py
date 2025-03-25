#Haz un programa que pida al usuario que ingrese una temperatura en
#grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
#mostrando el resultado.
print(' Bienvenido al programa que convierte los grados celcius en Fahrenheit')
ask = int(input('Ingrese la temperatura actual en grados celcius: '))

res = (ask * 1.8) + 32

print(f'La temperatura actual (°{ask}) en grados Fahrenheit es de {res}')