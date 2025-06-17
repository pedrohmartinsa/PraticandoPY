#Fila
#Firt In Firt Out
from time import sleep

lista_fila = [7, 9, 2, 6, 3]

while lista_fila:
    print(f'Atendendo: {lista_fila.pop(0)}')
    sleep(0.5)
print(lista_fila)