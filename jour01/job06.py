class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom
        print("L'âge de l'animal", self.age, "ans")
    def vieillir(self):
        self.grandir = self.age + 1
        print("L'âge de l'animal", self.grandir, "ans")
    def nommer(self, affprenom):
        self.affprenom = affprenom
        print("L'animal se nomme", affprenom)


init = Animal(0, "")
init.vieillir()
init.nommer("Luna")
