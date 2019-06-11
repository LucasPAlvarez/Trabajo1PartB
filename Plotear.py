import matplotlib.pyplot as plt
import json
import os

myInfo = {}

#carga los datos del json si existe
def loadJson():
	if os.path.isfile("Data/data.json"):
		with open("Data/data.json") as jFile:
			temp = json.load(jFile)
		return temp

#genera graficas de los datos importantes de la poblacion
def plotear(subject):
	#carga el json en una variable
	myInfo = loadJson()
	max = 0

	#genera una grafica con la info que se le pide
	plt.bar(range(len(myInfo[subject])), myInfo[subject], color = "g")
	for i in range(len(myInfo[subject])):
		if myInfo[subject][i] > max:
			max = myInfo[subject][i]

	plt.xlabel("Generaciones")
	plt.ylabel(subject)
	plt.axis([0, len(myInfo[subject]), 0, max+(max*10/100)])
	plt.show()