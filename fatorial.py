def fatorial(n):
	fatorial = 1
	while n > 1:
		fatorial = fatorial * n
		n = n - 1
	return fatorial


fatorialDe = 1
while fatorialDe != 0:
	fatorialDe = int(input('Digite um número para calcular seu fatorial: '))
	result = fatorial(fatorialDe)
	print (result)