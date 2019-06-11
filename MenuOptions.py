import Poblacion
import Plotear as plt
import SaveandLoad as SL
import os

#en este archivo se almacenan todas las opciones del menu

#crea una poblacion con los datos 
def createPoblacion():
	# te pide ingresar los datos de la poblacion a generar
	cant = 10
	probCrossover = float(input("ingrese la probabilidad de crossover\n"))
	if 0> probCrossover or probCrossover > 1:
		#probabilidad de crossover normal
		probCrossover = 0.75

	probMutation = float(input("ingrese la probabilidad de mutacion\n"))
	if 0> probMutation or probMutation > 1:
		#probabilidad de mutacion normal
		probMutation = 0.05
	
	#crea la poblacion
	poblacion = Poblacion.Poblacion(cant,probCrossover,probMutation)
	
	# borra la vieja generacion y guarda los datos de la nueva generacion
	cleanUp()
	SL.saveHistory(poblacion)
	text = poblacion.imprimirAll()
	print(text)
	SL.saveRecord(text)
	return poblacion 


#Crea una nueva generacion
def proximaGeneracion(poblacion, cant = 1):
	for i in range(cant):
		poblacion.nextGeneracion()
		text = poblacion.imprimirAll()
		print(text)
		SL.saveHistory(poblacion)
		SL.saveRecord(text)
	return 0

#elige que valor deseas representar en una grafica
def plotear():
	
	subject = input("que desea graficar?\n\t1)minValue\n\t2)Promedio\n\t3)MaxValue\n")
	if subject == "1":
		plt.plotear("minValue")
	elif subject == "2":
		plt.plotear("Promedio")
	elif subject == "3":
		plt.plotear("maxValue")

#limpia la carpeta data de los archivos de la generacion anterior 
def cleanUp():
	if os.path.isfile("Data/data.json"):
		os.remove("Data/data.json")
	if os.path.isfile("Data/pasado.txt"):
		os.remove("Data/pasado.txt")
