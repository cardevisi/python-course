#Todo número divisível por 2, é um número par.

n = int(input('Digite um número natural inteiro: '))
while n != 0:
    if n % 2 == 1:
        print(n,"é um número ímpar.")
    else:
        print(n, "não é um número ímpar.")
    n = int(input('Digite um número natural inteiro: '))