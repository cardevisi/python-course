num = int(input('Digite um numero: '))
resto = -1
soma = 0

while resto != 0:
	resto = num % 10
	num = num // 10
	print('RESTO: ', resto, 'NUM', num)
	soma = soma + resto
	

print('A soma de todos os digitos é: ', soma)