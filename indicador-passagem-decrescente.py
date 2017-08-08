##Indicadores de passagem são variáveis condicionais que determinam uma mudança ou a quebra de execução de um trecho de código. No exemplo abaixo enquanto a variável decrescente for verdadeira o loop irá solicitar ao usuário que preencha o próximo número da sequência. Quando esse condição é quebrada, ou seja quando o próximo número da sequência não estiver na ordem decrescente o loop é interempido, o valor da variável decrescente passa a ser False indicando a passagem de um estado para outro.

decrescente = True
anterior = int(input('Digite o primeiro número da sequência: '))

valor = 1

while valor != 0 and decrescente:
	valor = int(input('Digite o próximo número da sequência: '))
	if valor > anterior:
		decrescente  = False
	anterior = valor

if decrescente == True:
	print('A sequência está em ordem descrecente')
else:
	print('A sequência não está em ordem descrecente')