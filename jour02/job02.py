class Livre:
    def __init__(self, titre, auteur, numpage):
        self.__titre = titre
        self.__auteur = auteur
        self.__numpage = numpage
    #Assesseurs
    def getTitre(self):
        return self.__titre 
    def getAuteur(self):
        return self.__auteur
    def getPages(self):
            return self.__numpage
    #Mutateurs
    def setTitre(self, titre):
        self.__titre = titre
    def setAuteur(self, auteur):
        self.__auteur = auteur
    def setPages(self, numpage):
        self.__numpage = numpage

init = Livre("Livre1", "Auteur1", 5)
print("Le titre du livre est", init.getTitre())
print("L'auteur du livre est", init.getAuteur())
print("Le nombre de pages du livre est", init.getPages())
init.setTitre("Livre2")
init.setAuteur("Auteur2")
init.setPages(-1)
print("Le titre du livre est", init.getTitre())
print("L'auteur du livre est", init.getAuteur())
print("Le nombre de pages du livre est", init.getPages())