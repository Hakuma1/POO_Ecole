from Personne import Personne


class Professeur(Personne):
    def __init__(self, nom, sexe, tarif):
        Personne.__init__(self, nom, sexe)
        self.tarif = tarif

    def __str__(self):
        return Personne.__str__(self) + f"Mon tarif est de {self.tarif}dh."
