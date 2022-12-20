from Personne import Personne


class Etudiant(Personne):
    def __init__(self, nom, sexe, niveau):
        Personne.__init__(self, nom, sexe)
        self.niveau = niveau

    def __str__(self):
        return Personne.__str__(self) + f"Je suis\
 actuellement en {self.niveau}."
