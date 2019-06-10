import random
import Cromosoma

class Poblacion:

	def __init__ (self, cant, probCrossover = 0.75, probMutation = 0.05):
		self.poblacion = []
		self.numGeneracion = 0
		self.probCrossover = probCrossover
		self.probMutation = probMutation

		for i in range(cant):
			self.poblacion.append(Cromosoma.Cromosoma())

		self.totalFitness = self.totalFitness()
		self.promedioFitness = self.totalFitness/len(self.poblacion)

	def __str__(self):
		temp = ""
		for cromosoma in self.poblacion:
			for num in cromosoma:
				temp += num.__str__()

	def __getitem__(self, index):
		return self.poblacion[index]

	def totalFitness(self):
		fitness = 0
		for crom in self.poblacion:
			fitness += crom.valorFuncion()
		return fitness

	def cromosomaFitness(self, crom):
		return crom.valorFuncion()/self.totalFitness

	def nextGeneracion(self):
		nextGen = []

		pasedirecto = self.paseDirecto()

		for cromo in pasedirecto:
			nextGen.append(cromo)

		ruleta = self.generarRuleta()

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

		if len(nextGen) == len(self.poblacion):
			self.poblacion = nextGen
		else:
			self.poblacion = nextGen
			print("hubo un error con la cantidad")

		self.numGeneracion +=1
		return 0


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
		return [pase1,pase2]

	def generarRuleta(self):
		ruleta = []
		for i in range(len(self.poblacion)):
			ruleta += [i] *int(float(self.cromosomaFitness(self.poblacion[i]))* 100)

		return ruleta

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
		strDevolver += "Promedio\t\t\t\t\t\t{0:.4f}\t0.1\n".format(sumaTemp/len(self.poblacion))
		strDevolver += "Maximo\t\t\t\t\t\t\t{0:.4f}\t{1}\n".format(maximoTemp.valorFuncion(), "{:.2}".format(maximoTemp.valorFuncion()/self.totalFitness))

		#devuelve el string puede verse en pantalla o guardarse en un .txt
		return strDevolver