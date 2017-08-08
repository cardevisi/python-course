#Todo número divisível por 2, é um número par.

n = int(input('Digite um número natural inteiro: '))
while n != 0:
    if n % 2 == 0:
        print(n,"é um número par.")
    else:
        print(n, "não é um número par.")
    n = int(input('Digite um número natural inteiro: '))