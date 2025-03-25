#Implementa un programa que solicite al usuario que ingrese una lista de
#números. Luego, imprime la lista pero detén la impresión si encuentras un
#número negativo. Nota: utilice la sentencia break cuando haga falta.

lista = []
while(True):
        lista.append(int(input('Ingrese un numero: ')))
        if(lista[len(lista)-1])==0:
                lista.remove(0)
                break

for i in lista:
        if(i>0):
                print(i)
                continue
        print(f'Finalizando impresion... encontre {i}')
        break