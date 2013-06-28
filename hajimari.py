import random

class particle:
	def __init__(self, x, y, z):
		self.kind = 1 
		self.magnitude = random.randint(0, 1000)
		self.x = x
		self.y = y
		self.z = z
	def __repr__(self):
		return "[Particle: %s] x: %s y: %s z: %s  [Magnitude: %s] " % (str(self.kind), str(self.x), str(self.y), str(self.z), str(self.magnitude))
