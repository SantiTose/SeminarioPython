#Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
#listas, una con los número pares y otras con los que son impares. Imprima
#las listas al terminar de procesarlas

lista = [1,2,3,4,5,6,7,8,9,11,12,13,14,15]
listaPar = []
listaImpar = []
x = -1

for i in lista:
    if(i % 2)==0:
        listaPar.append(i)
        continue
    listaImpar.append(i)

print(f'Lista de impares : {listaImpar}')
print(f'Lista de pares: {listaPar}')
