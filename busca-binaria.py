#Algortimo de busca binária

lista_ordenada = [-100, 10, 20, 33, 40, 55, 60, 70]

def buscaBinaria(lista, x):
    primeiro = 0
    ultimo = len(lista)-1
    
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return -1

print(buscaBinaria(lista_ordenada, 55))