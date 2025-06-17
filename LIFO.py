#Pilha
#Last In First Out
from time import sleep

lista_pilha = [0, 1, 2, 3, 4]

for i in range((len(lista_pilha) -1), -1, -1):
    print(f'atendendo: {lista_pilha[i]}')
    lista_pilha.pop()
    sleep(0.5)
print(lista_pilha)