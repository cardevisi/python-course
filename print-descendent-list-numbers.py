num = int(input('Digite uma sequência de números inteiros: '))
list = []
while num != 0:
    list.append(num)
    num = int(input('Digite uma sequência de números inteiros: '))

print('\n', list, '\n')

index = len(list)-1
while index >= 0:
    print(index, list[index])
    index = index - 1