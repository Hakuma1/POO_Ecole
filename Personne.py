class Personne:
    def __init__(self, nom, sexe):
        self.nom = nom
        self.sexe = sexe

    def __str__(self):
        return f"Je m'appelle {self.nom}.\
 Je suis un {self.sexe}. "
