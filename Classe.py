class Classe:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau

    def __str__(self):
        return f"Il s'agit de la classe {self.nom} du niveau {self.niveau}."