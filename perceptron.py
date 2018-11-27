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
			tab[i][j] = random.uniform(-1,1)
	return tab
			
def propagation(poids,retine):
	sortie = 0
	for i in range(4):
		for j in range(5):
			sortie = sortie + poids[i][j]*retine[i][j]
	#Biais
	sortie = sortie + random.uniform(-1,1)
	print(sortie)
	if(sortie >= 0.5):
		sortie = 1
	else:
		sortie = 0
	return sortie
	
if __name__ == '__main__' :
	c = copieInRetine('c')
	a = copieInRetine('a')
	poids = aleaPoids();
	print(poids)
	print(propagation(poids,a))
