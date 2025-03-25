#Escribe un programa que tome una lista de números enteros como entrada
#del usuario. Luego, convierte cada número en la lista a string y únelos en
#una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
#número que sea múltiplo de 3 de la cadena final.

lista=[]
cant = int(input('Ingrese la cantidad de elementos de la lista: '))
for i in range(cant):
    lista.append(int(input('Ingrese un numero: ')))

for index,i in enumerate(lista): # La funcion enumerate en los bucles for me devuelve primero el indice y luego el valor
    lista[index] = str(i)
    
aux = ''
for i in lista:
    if((int(i)) % 3)!=0:
        if(i == lista[len(lista)-1]):#Pregunto si es el ultimo para no agregar el gion al final
            aux+=i
            break
        aux += i + ' - '

print(aux)
