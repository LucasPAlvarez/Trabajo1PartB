import Poblacion
import MenuOptions
import os

def startUp():
	if not os.path.exists("Data"):
		os.makedirs("Data")

	poblacion = MenuOptions.createPoblacion()
	return poblacion


def Menu(poblacion):
	while True: 
		c = input("que desea hacer:\n\n\t1) Generar nuevas genraciones.\n\t2) Plotear\n\t3) Nueva poblacion\n\t4) Salir\n" )
	
		if c == "1":
			MenuOptions.proximaGeneracion(poblacion)
		elif c == "2":
			MenuOptions.plotear()
		elif c == "3":
			poblacion = MenuOptions.createPoblacion()
			
		elif c == "4":
			break

poblacion = startUp()
Menu(poblacion)