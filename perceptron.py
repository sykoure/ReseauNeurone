import csv
import numpy as np
import random

def copieInRetine(fichier):
	if(fichier == 'a'):
		M = np.loadtxt('A.txt')
	elif(fichier == 'c'):
		M = np.loadtxt('C.txt')
	else:
		return 0
	return M
	
def aleaPoids():
	tab = [[0 for k in range(5)] for k in range(4)]
	for i in range(4):
		for j in range(5):
			tab[i][j] = random.uniform(0,1)
	return tab
			

if __name__ == '__main__' :
	c = copieInRetine('c')
	a = copieInRetine('a')
	poids = aleaPoids();

	neuroneSortie
