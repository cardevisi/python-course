#As temperaturas em Fahrenheit são utilizadas em países colonizados pelos britênicos e atualmente é utilizada em poucos países de língua inglesa como os Estados Unidos e Belize.

# Fórmula para comversão de temperatura
#  C    F - 32
# --- = ------
#  5	  9

F = float(input('Digite uma temperatura em Fahrenheit: '))
C = (F - 32) * 5 / 9

print('A temperatura e Celsius é ', C)