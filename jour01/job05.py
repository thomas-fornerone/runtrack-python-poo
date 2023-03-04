from random import randint

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def afficherLesPoints(self):
		print("Les coordonnées sont en x :", self.x, "et en y :", self.y)
	def afficherX(self):
		print("Coordonnée x :", self.x)
	def afficherY(self):
		print("Coordonnée y :", self.y)
	def changerX(self):
		self.x2 = input()
		print("La coordonnée x est désormais :", self.x2)
	def changerY(self):
		self.y2 = input()
		print("La coordonnée y est désormais :", self.y2)
		
init = Point(24, 67)
init.afficherLesPoints()
init.afficherX()
init.afficherY()
init.changerX()
init.changerY()
