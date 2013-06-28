import random
import math
import sys

class Sim:
	def __init__(self, size):
		self.size = size
		self.resources = []
		self.part = particle()
		
	def step(self):
		if random.randint(0,1000) > 500:
			self.resources.append(resource(self.size))
		if len(self.resources) > 0:
			self.part.step(self.resources[0])
			if self.part.consumed == True:
				self.resources.pop(0)
	
	def __repr__(self):
		string = ""
		string += self.part.__repr__()
		string += "\n" * 2
		for s in self.resources:
			string += s.__repr__() + "\n"
		return string




class resource:

	def __init__(self, size):
		self.x = random.randint(0,size)
		self.y = random.randint(0,size)
		self.energy = random.randint(0,100)

	def __repr__(self):
		return "[E: %s] x:  %s\ty:  %s" % (self.energy, self.x, self.y)


class particle:
	def __init__(self):
		self.speed = 1
		self.x = 50
		self.y = 50
		self.energy = 0
		self.consumed = False

	def step(self, res):
		self.chase(res)
		if self.x == res.x and self.y == res.y:
			self.consumed = True		
			self.energy += res.energy
			self.speed = self.energy / 20
			if self.speed < 1:
				self.speed = 1
		else:
			self.consumed = False

	def chase(self, res):
		self.x = self.move(self.x, res.x)
		self.y = self.move(self.y, res.y)
	
	def move(self, p1, p2):
		if math.fabs(p1 - p2) < self.speed:
			p1 = p2
		elif p1 > p2:
			p1 -= self.speed
		else:
			p1 += self.speed
		return p1
	def __repr__(self):
		return "[Energy: %s] x: %s\ty: %s" % (self.energy, self.x, self.y)


sim = Sim(100)
while True:
	sim.step()
	print('\n' * 100)
	print sim
	sys.stdin.read(1)
