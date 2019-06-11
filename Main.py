import Poblacion
import MenuOptions
import os

#inicializa todo lo necesario para que el programa comienze
def startUp():
	#Crea la carpeta que almacena los datos de la poblacion si no existe
	if not os.path.exists("Data"):
		os.makedirs("Data")

	#inicializa la poblacion 
	poblacion = MenuOptions.createPoblacion()
	return poblacion


def Menu(poblacion):
	while True: 
		c = input("que desea hacer:\n\n\t1) Generar nuevas genraciones.\n\t2) Plotear\n\t3) Nueva poblacion\n\t4) Salir\n" )
	
		if c == "1":
			#crea nuevas generaciones de la poblacion 
			MenuOptions.proximaGeneracion(poblacion)
		elif c == "2":
			#muestra los datos de la poblacion en una grafica
			MenuOptions.plotear()
		elif c == "3":
			#crea una nueva poblacion
			poblacion = MenuOptions.createPoblacion()
			
		elif c == "4":
			#sale del programa
			MenuOptions.cleanUp()
			break


#esto utiliza los dos metodos creados anteriormente
poblacion = startUp()
Menu(poblacion)