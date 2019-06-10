import Poblacion
import os
import json

#Guarda todas las generaciones para poder verlas en un archivo .txt
def saveRecord(texto):
	if not os.path.isfile("Data/pasado.txt"):
		pathFile = open("Data/pasado.txt", "w")
	else:
		pathFile = open("Data/pasado.txt", "a")


	pathFile.write(texto)
	pathFile.write("\n\n")

	pathFile.close()


#Guarda todas las generaciones para poder representarlas en una grafica
def saveHistory(myPobl):
	#Configura algunos valores para guardar
	prome = 0
	mValue = 0
	lValue = 2
	for pob in myPobl.poblacion:
		temp = pob.valorFuncion()
		if mValue < temp:
			mValue = temp
		if lValue > temp:
			lValue = temp
		prome = prome + temp


	#Si no hay un archivo json, entonces crea datos nuevos
	if not os.path.isfile("Data/data.json"):
		newData ={"minValue":[], "Promedio":[], "maxValue":[]}
		
	else:
		with open("Data/data.json") as jl:
			newData = json.load(jl)

	#Añade los datos nuevos y luego los guarda
	newData["minValue"].append(lValue)
	newData["Promedio"].append(prome/4)
	newData["maxValue"].append(mValue)
	with open("Data/data.json", "w") as sj:
		json.dump(newData, sj)