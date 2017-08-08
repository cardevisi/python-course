#Número primo é um número inteiro que admite exatamente 4 divisores:

#Os divisores são 1 e o próprio número:

#Uma das maneiras de verificar se um número é primo é dividí-lo pela sequência de números naturais por exemplo, 2, 3, 4, 5, e analisar se algum deles divisível. Se for divisível, ou seja, se o modúlo for diferente de zero, significa que este número não é primo.

def ePrimo(x):
    fator = 2
    if x == 2:
        return True

    while  n % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True



n = int(input('Digite um número inteiro: '))
while  n != 0:
    if ePrimo(n):
        print(n,'é um número primo.')
    else:
        print(n,'não é um número primo.')
    n = int(input('Digite um número inteiro: '))

