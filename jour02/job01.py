class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def getLongueur(self):
        return self.__longueur 
    def getLargeur(self):
        return self.__largeur
    def setLongueur(self, longueur):
        self.__longueur = longueur
    def setLargeur(self, largeur):
        self.__largeur = largeur
init = Rectangle(10, 5)
print("La longueur est égale à", init.getLongueur())
print("La largeur est égale à", init.getLargeur())
init.setLongueur(34)
init.setLargeur(23)
print("La longueur est égale à", init.getLongueur())
print("La largeur est égale à", init.getLargeur())