arr = [1, 2, 3, 4, 6]
print(arr, 'Length:', len(arr))

arr.append(10)

#ordem acendente
i = 0
while i < len(arr):
	print(arr[i])
	i = i + 1

#ordem descendente
i = len(arr)-1
#print('\n', i)
while i != 0:
	print(arr[i])
	i = i - 1
	
