import random

class resources:

	def __init__(self):
		self.resources = []

	def findChase(self):
		if len(self.resources) == 0:
			return None
		return self.resources[self.in_res()]

	def in_res(self):
		return random.randint(0, len(self.resources) - 1)

	def consume(self, res):
		self.resources.remove(res)

	def has_res(self):
		return len(self.resources) > 0
	
	def add_resource(self, size):
		self.resources.append(resource(size))
	
	def __repr__(self):
		string = ""
		for s in self.resources:
			string += s.__repr__() + "\n"
		return string
	
	
		
class resource:
	def __init__(self, size):
		self.x = random.randint(0,size)
		self.y = random.randint(0,size)
		self.chasing = 0
		self.consumed = False
		self.energy = random.randint(0,100)
		
	def chase(self):
		self.chasing += 1

	def consume(self):
		self.consumed = True
	
	def __repr__(self):
		if self.chasing > 0:
			return "[E: %s] x:  %s\ty:  %s [Chasing: %s]" % (self.energy, self.x, self.y, self.chasing)
		return "[E: %s] x:  %s\ty:  %s" % (self.energy, self.x, self.y)
		
