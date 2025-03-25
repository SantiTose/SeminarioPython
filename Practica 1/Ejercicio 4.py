#Cree un programa que dada una lista de números imprima sólo los que son
#pares. Nota: utilice la sentencia continue donde haga falta.

lista = []
x = -1
while(x!=0):
    x = int(input('Ingrese un numero para agregar a la lista: '))
    lista.append(x)
print('Encontre todos estos pares: ')
for i in lista:
    if(i % 2)!= 0:
        continue
    print(f'{i}',end=', ')
