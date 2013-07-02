import math

class particle:
	def __init__(self, energy=50):
		self.speed = 1
		self.x = 50
		self.y = 50
		self.energy = energy
		self.is_chasing = False 
		self.can_consume = False
		self.spawn = False
		self.res = None
		self.metabolism_count  = 0

	def step(self):
		if self.res != None:
			if self.res.consumed == False:
				self.chase(self.res)
				if self.checkConsume():
					self.consume()
				self.can_consume = self.checkConsume()
			else:
				self.is_chasing = False
				self.res = None
		self.metabolism()
		self.trySpawn()
		
			
	def metabolism(self):
		self.metabolism_count += 1
		if self.metabolism_count > 3:
			self.energy -= 1
			self.calcspeed()
			self.metabolism_count = 0
	def checkConsume(self):
		return self.x == self.res.x and self.y == self.res.y

	def chase(self, res):
		self.x = self.move(self.x, res.x)
		self.y = self.move(self.y, res.y)
	
	def chaseRes(self, ress):
		self.res = ress
		self.res.chase()
		self.is_chasing = True
		
	def consume(self):
		self.energy += self.res.energy
		self.calcspeed()
		self.is_chasing = False
		self.res.consumed = True
	
	def move(self, p1, p2):
		if math.fabs(p1 - p2) < self.speed:
			p1 = p2
		elif p1 > p2:
			p1 -= self.speed
		else:
			p1 += self.speed
		return p1

	def trySpawn(self):
		if self.energy > 1500:
			self.spawn = True
		else:
			self.spawn = False
	
	def spawnnew(self):
		self.energy -= 1500
		self.calcspeed()
		return particle(50)
	
	def calcspeed(self):
		self.speed = self.energy / 60
		if self.speed < 1:
			self.speed = 1


	def __repr__(self):
		return "[Energy: %s] x: %s\ty: %s" % (self.energy, self.x, self.y)
