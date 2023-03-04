class Personne:
	def __init__(self, prenom, nom):
		self.nom = nom
		self.prenom = prenom
	def SePresenter(self):
		print("Je suis", self.prenom, self.nom)
initialisation = Personne("John", "Doe")
initialisation.SePresenter()
initialisation = Personne("Jean", "Dupond")
initialisation.SePresenter()