list = [0,1,2,3,5,6,10]

def busca_sequencial(seq, x):
	for i in range(len(seq)):
		if seq[i] == x:
			return True
	return False

print (busca(list, 15))