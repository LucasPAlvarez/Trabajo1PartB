import random
import math

class Cromosoma:

	def __init__(self, cant = 30):
		self.cromosoma = []
		for i in range(cant):
			self.cromosoma.append(random.randint(0,1))

	def __str__(self):
		temp = ""
		for num in self.cromosoma:
			temp += num.__str__()
		return temp

	def __iter__(self):
		return iter(self.cromosoma)

	def __getitem__(self, index):
		return self.cromosoma[index]

	def valorDecimal(self):
		sumaTemp = 0
		for i in range(len(self.cromosoma)):
			sumaTemp += math.pow(2,i) * self.cromosoma[(len(self.cromosoma)-1)-i]
		return int(sumaTemp) 

	def valorFuncion(self):
		coef = (2**30)-1
		return math.pow(self.valorDecimal()/coef, 2)

	def Mutacion(self):
		index = random.randint(0,len(self.cromosoma)-1)
		self.cromosoma[index] = abs(self.cromosoma[index] - 1)