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
	if(sortie <= 0):
		sortie = 0
	else:
		sortie = 1
	return sortie

def apprentissage(poids,retine,retine2,expectedOuputa,expectedOuputc):
	sortie = 0
	choix_retine = 1
	sortie = propagation(poids,retine)
	for i in range(10000):
		if((sortie == 0)and(choix_retine == 1)):
			for i in range(4):
				for j in range(5):
					poids[i][j] = poids[i][j] + 0.1 * (expectedOuputa - sortie) * retine[i][j]
					choix_retine = choix_retine * -1
		elif((sortie == 1)and(choix_retine == -1)):
			for i in range(4):
				for j in range(5):
					poids[i][j] = poids[i][j] + 0.1 * (expectedOuputc - sortie) * retine2[i][j]
					choix_retine = choix_retine * -1
		else:
			i = 10000
	return poids

if __name__ == '__main__' :

	expectedValueA = 1.0
	expectedValueC = 0.0
	c = copieInRetine('c')
	a = copieInRetine('a')

	poids = aleaPoids()
	print(poids)
	
	apprentissage(poids,a,c,expectedValueA,expectedValueC)

	print(poids)
	print(propagation(poids,a))
