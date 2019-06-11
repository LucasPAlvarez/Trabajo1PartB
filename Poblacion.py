import random
import Cromosoma

class Poblacion:
	#inicializa la poblacion y todas sus variables
	def __init__ (self, cant, probCrossover = 0.75, probMutation = 0.05):
		self.poblacion = []
		self.numGeneracion = 0
		self.probCrossover = probCrossover
		self.probMutation = probMutation

		for i in range(cant):
			self.poblacion.append(Cromosoma.Cromosoma())

		self.totalFitness = self.totalFitnessfuncion()
		self.promedioFitness = self.totalFitness/len(self.poblacion)

	#permite convertir la poblacion en un string
	def __str__(self):
		temp = ""
		for cromosoma in self.poblacion:
			for num in cromosoma:
				temp += num.__str__()

	#permite buscar en poblacion por index
	def __getitem__(self, index):
		return self.poblacion[index]

	#calcula el fitness de todos los genes y los suma
	def totalFitnessfuncion(self):
		fitness = 0
		for crom in self.poblacion:
			fitness += crom.valorFuncion()
		return fitness

	#calcula el porcentaje del fitness de un cromosoma
	def cromosomaFitness(self, crom):
		return crom.valorFuncion()/self.totalFitness


	#crea una nueva generacion
	def nextGeneracion(self):
		#crea una nueva generacion vacia
		nextGen = []

		#selecciona los cromosomas para el pase directo
		pasedirecto = self.paseDirecto()

		for cromo in pasedirecto:
			nextGen.append(cromo)

		#crea una ruleta para la creacion de hijos
		ruleta = self.generarRuleta()

		#crea los hijos haciendo crossover  mutando los padres seleccionados al azar en la ruleta
		cantHijos = int((len(self.poblacion)-2)/2)
		for i in range(cantHijos):
			padres = []
			padres.append(self.poblacion[random.choice(ruleta)])
			padres.append(self.poblacion[random.choice(ruleta)])

			if random.random() > self.probCrossover:
				hijos = self.Crossover(padres)
			else:
				hijos = padres
			for cromo in hijos:
				if random.random() > self.probMutation:
					cromo.Mutacion()

			for cromo in hijos:
				nextGen.append(cromo)

		#guarda la nueva generacion en la variable poblacion

		if len(nextGen) == len(self.poblacion):
			self.poblacion = nextGen
		else:
			self.poblacion = nextGen
			print("hubo un error con la cantidad")

		self.numGeneracion +=1
		self.totalFitness = self.totalFitnessfuncion()
		self.promedioFitness = self.totalFitness/len(self.poblacion)
		return 0

	# los 2 mejores cromosomas selecionados por su fitness son seleccionados para pasar directamente a la siguiente generacion
	def paseDirecto(self):
		pase1 = self.poblacion[0]
		pase2 = self.poblacion[1]
		for index in range(2,len(self.poblacion),1):
			pruevaPase = self.poblacion[index]
			if(self.cromosomaFitness(pase1)< self.cromosomaFitness(pruevaPase)):
				temp = pase1
				pase1 = pruevaPase
				pruevaPase = temp

			if(self.cromosomaFitness(pase2)< self.cromosomaFitness(pruevaPase)):
				pase2 = pruevaPase
		print("\nel primer valor es: {0} elsegundo valor es: {0}\n\n".format(pase1.valorDecimal(), pase2.valorDecimal()))
		return [pase1,pase2]


	#genera la ruleta que se utilizara para selecionar los padres
	def generarRuleta(self):
		ruleta = []
		for i in range(len(self.poblacion)):
			ruleta += [i] *int(float(self.cromosomaFitness(self.poblacion[i]))* 100)

		return ruleta

	#hace el crossover de dos padres
	def Crossover(self, padres):
		crossPoint = random.randint(0,len(self.poblacion)-1)
		hijos = [Cromosoma.Cromosoma(),Cromosoma.Cromosoma()]
		for loop in range(2):
			for index in range(len(padres[0].cromosoma)-1):
				if index < crossPoint:
					hijos[loop].cromosoma[index] = padres[loop].cromosoma[index]
				else:
					hijos[loop].cromosoma[index] = padres[1-loop].cromosoma[index]
		return hijos


	def imprimirAll(self):
		#devuelve un string con todos los datos de la generacion de forma ordenada
		#variables temporales para almacenar otros datos
		strDevolver = ""
		sumaTemp = 0
		maximoTemp = self.poblacion[0]

		# strDevolver almacena todo lo que se va a inprimir
		strDevolver += "generacion {0}\n".format(self.numGeneracion)
		strDevolver += "---------------\n\n"
		strDevolver += "Cromosoma\t\t\t\tValor\t\tFuncion\tFitness\n"
		strDevolver += "_________________________________________________________________________\n"

		#muestra cada cromosoma con sus datos dentro de poblacion
		for i in self.poblacion:
			strDevolver += "{0}\t\t".format(i)
			strDevolver += "{0}\t".format(i.valorDecimal())
			strDevolver += "{0:.4f}\t".format(i.valorFuncion())
			#sumaTemp almacena la suma del valor de los cromosomas evaluados en la funcion
			sumaTemp += i.valorFuncion()
			#maximo guarda el maximo de los cromosomas
			if(maximoTemp.valorFuncion() < i.valorFuncion()):
				maximoTemp = i
			strDevolver += "{:.2}\n".format(self.cromosomaFitness(i))

		strDevolver += "_________________________________________________________________________\n"
		strDevolver += "Suma\t\t\t\t\t\t\t{0:.4f}\t1\n".format(sumaTemp)
		#strDevolver += "Promedio\t\t\t\t\t\t{0:.4f}\t0.1\n".format(sumaTemp/len(self.poblacion))
		strDevolver += "Promedio\t\t\t\t\t\t{0:.4f}\t0.1\n".format(self.promedioFitness)
		strDevolver += "Maximo\t\t\t\t\t\t\t{0:.4f}\t{1}\n".format(maximoTemp.valorFuncion(), "{:.2}".format(maximoTemp.valorFuncion()/self.totalFitness))

		#devuelve el string puede verse en pantalla o guardarse en un .txt
		return strDevolver