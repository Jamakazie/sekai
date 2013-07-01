import random
import math
import sys
from particles import particle
from resources import resource

class Sim:
	def __init__(self, size):
		self.size = size
		self.resources = resource.resources()
		self.part = []
		self.part.append(particle.particle())
		
	def step(self):
		if random.randint(0,1000) > 500:
			self.resources.add_resource(self.size)
		if self.resources.has_res():
			for part in self.part:
				if self.resources.has_res() == False:
					continue
				if part.is_chasing == False:
					part.chaseRes(self.resources.findChase())
				part.step()
				if part.res != None:
					if part.res.consumed == True:
						self.resources.consume(part.res)
				if part.spawn == True:
					self.part.append(part.spawnnew())
	
	def __repr__(self):
		string = ""
		for part in self.part:
			string += part.__repr__()
			string += "\n" 
			
		string += "\n" * 2
		string += self.resources.__repr__() 
		return string



sim = Sim(100)
while True:
	sim.step()
	print('\n' * 100)
	print sim
	sys.stdin.read(1)
