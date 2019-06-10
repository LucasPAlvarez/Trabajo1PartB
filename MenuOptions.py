import Poblacion
import Plotear as plt
import SaveandLoad as SL

def createPoblacion():
	cant = int(input("ingrese la cantidad de cromosomas en la poblacion\n"))
	probCrossover = float(input("ingrese la probabilidad de crossover\n"))
	if 0> probCrossover or probCrossover > 1:
		#probabilidad de crossover normal
		probCrossover = 0.75

	probMutation = float(input("ingrese la probabilidad de mutacion\n"))
	if 0> probMutation or probMutation > 1:
		#probabilidad de mutacion normal
		probMutation = 0.05
	
	poblacion = Poblacion.Poblacion(cant,probCrossover,probMutation)
	SL.saveHistory(poblacion)
	text = poblacion.imprimirAll()
	print(text)
	SL.saveRecord(text)
	return poblacion 



def proximaGeneracion(poblacion, cant = 1):
	for i in range(cant):
		poblacion.nextGeneracion()
		text = poblacion.imprimirAll()
		print(text)
		SL.saveHistory(poblacion)
		SL.saveRecord(text)
	return 0


def plotear():
	
	subject = input("que desea graficar?\n\t1)minValue\n\t2)Promedio\n\t3)MaxValue\n")
	if subject == "1":
		plt.plotear("minValue")
	elif subject == "2":
		plt.plotear("Promedio")
	elif subject == "3":
		plt.plotear("maxValue")