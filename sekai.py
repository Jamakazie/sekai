import random
import sys
from hajimari import particle


class sekai():
	def __init__(self):
		self.particles = []
		firstparticle = particle(0,0,0)
		self.particles.append(firstparticle)
	def step(self):
		#self.gravity(self.particles)
		if random.randint(0,1000) > 900:
			self.particles.append(particle(random.randint(-1000,1000), random.randint(-1000,1000), random.randint(-1000,1000)))
			print "new particle added!"
	def gravity(self, point1, point2):
		pass
		#force = 100
	
	def __repr__(self):
		s = ""
		for p in self.particles:
			s += str(p) + "\n"
		return s

s = sekai()
while(True):
	s.step()
	print('\n'*100)
	print s
	sys.stdin.read(1)


