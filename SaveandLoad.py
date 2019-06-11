import Poblacion
import os
import json

#Guarda todas las generaciones para poder verlas en un archivo .txt
def saveRecord(texto):
	#busca el archivo .txt, si no lo encuentra crea uno nuevo sino lo abre solo para editarlo
	if not os.path.isfile("Data/pasado.txt"):
		pathFile = open("Data/pasado.txt", "w")
	else:
		pathFile = open("Data/pasado.txt", "a")

	#escribe el texto dado a la funcion
	pathFile.write(texto)
	pathFile.write("\n\n")

	#cierra el archivo
	pathFile.close()


#Guarda todas las generaciones en un archivo json para poder representarlas en una grafica
def saveHistory(myPobl):
	#saca los valores minimos y maximos de la poblacion
	mValue = 0
	lValue = 2
	for pob in myPobl.poblacion:
		temp = pob.valorFuncion()
		if mValue < temp:
			mValue = temp
		if lValue > temp:
			lValue = temp


	#Si no hay un archivo json, entonces crea datos nuevos,si existe lo abre para agregarle mas datos
	if not os.path.isfile("Data/data.json"):
		newData ={"minValue":[], "Promedio":[], "maxValue":[]}
		
	else:
		with open("Data/data.json") as jl:
			newData = json.load(jl)

	#Añade los datos nuevos y luego los guarda
	newData["minValue"].append(lValue)
	newData["Promedio"].append(myPobl.promedioFitness)
	newData["maxValue"].append(mValue)
	with open("Data/data.json", "w") as sj:
		json.dump(newData, sj)