#A sequência de Fibonacci é uma sequência de números inteiros que geralmente se inicia a partir do 0 e 1.


def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

#
#print('fibo', fibo(2))
#print('fibo', fibo(5))
#print('fibo', fibo(10))
#print('fibo', fibo(100))
#
#
# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    print(a, b)
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(5)